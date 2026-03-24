import os
import re
import threading
import pdfplumber
import customtkinter as ctk
from tkinter import filedialog
import arabic_reshaper
from bidi.algorithm import get_display

# إعدادات المظهر
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")  # غيرتلك اللون للأخضر ليطلع أحلى

class InvoiceOrganizerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # إعدادات النافذة
        self.title("Abdullah's Ultimate Archiver")
        self.geometry("700x550")
        
        self.selected_folder = ""

        # تخطيط الشبكة
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # === العنوان ===
        # نستخدم دالة fix_text لكل نص عربي
        self.label_title = ctk.CTkLabel(self, text=self.fix_text("أداة الأرشفة الذكية"), font=("IBM Plex Sans Arabic SemiBold", 28))
        self.label_title.grid(row=0, column=0, padx=20, pady=20)

        # === منطقة الأزرار ===
        self.frame_top = ctk.CTkFrame(self)
        self.frame_top.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.frame_top.grid_columnconfigure(0, weight=1)
        
        # الأزرار (لاحظ كيف قلبنا الترتيب بالـ Grid عشان يتناسب مع العين العربية)
        self.btn_start = ctk.CTkButton(self.frame_top, text=self.fix_text("ابدأ الفرز الآن "), command=self.start_thread, state="disabled", fg_color="#082418", hover_color="#16583C", font=("IBM Plex Sans Arabic SemiBold", 14))
        self.btn_start.grid(row=2, column=0, padx=10, pady=10)  # الزر الأخضر عاليسار

        self.label_path = ctk.CTkLabel(self.frame_top, text=self.fix_text(" لم يتم اختيار مجلد ... "), text_color="gray", font=("IBM Plex Sans Arabic SemiBold", 12))
        self.label_path.grid(row=1, column=0, padx=10, pady=10)

        self.btn_browse = ctk.CTkButton(self.frame_top, text=self.fix_text("اختر المجلد"), command=self.select_directory,fg_color="#124E34", font=("IBM Plex Sans Arabic SemiBold", 14), width=280,   # العرض بالبكسل (دبل الـ 140)
    height=60)
        self.btn_browse.grid(row=0, column=0, padx=10, pady=10) # زر الاختيار عاليمين

        # === الشاشة السوداء (Log) ===
        self.textbox_log = ctk.CTkTextbox(self, width=600, corner_radius=10, font=("IBM Plex Sans Arabic SemiBold", 14))
        self.textbox_log.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
        self.textbox_log._textbox.tag_configure("rtl", justify="right")
        self.log("مرحباً بك! الرجاء اختيار المجلد للبدء ...")

        # === شريط التحميل ===
        self.progressbar = ctk.CTkProgressBar(self)
        self.progressbar.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        self.progressbar.set(0)

    def fix_text(self, text):
        """دالة لإصلاح النص العربي - توصيل الحروف والاتجاه"""
        try:
            reshaped_text = arabic_reshaper.reshape(text)
            bidi_text = get_display(reshaped_text)
            return bidi_text
        except:
            # في حالة الفشل، نعيد النص الأصلي
            return text

    def log(self, message):
        # للكتابة في اللوج، نعالج النص أيضاً
        fixed_msg = self.fix_text(message)
        self.textbox_log.insert("end", fixed_msg + "\n", "rtl")
        self.textbox_log.see("end")

    def select_directory(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.selected_folder = folder_selected
            folder_name = os.path.basename(folder_selected)
            self.label_path.configure(text=self.fix_text(f"مجلد: {folder_name}"), text_color="white")
            self.btn_start.configure(state="normal")
            self.log(f"تم اختيار المجلد: {folder_name}")

    def start_thread(self):
        self.btn_start.configure(state="disabled")
        self.progressbar.start()
        thread = threading.Thread(target=self.run_organizer_logic)
        thread.start()

    def run_organizer_logic(self):
        folder_path = self.selected_folder
        self.log("========================================")
        self.log("🚀 جاري بدء عملية الفرز...")
        
        senders_keywords = {
# === 🎓 0. الجامعات والمؤسسات التعليمية (University Logic) ===
        
        # --- A. جامعات برلين (Berlin Specific) ---
        "HTW_Berlin": ["HTW Berlin", "Hochschule für Technik und Wirtschaft", "HTW-Berlin"],
        "FU_Berlin": ["Freie Universität Berlin", "FU Berlin"],
        "TU_Berlin": ["Technische Universität Berlin", "TU Berlin"],
        "HU_Berlin": ["Humboldt-Universität", "HU Berlin"],
        "Beuth_Hochschule": ["Beuth Hochschule", "Beuth University", "Berliner Hochschule für Technik", "BHT"],
        "HWR_Berlin": ["HWR Berlin", "Hochschule für Wirtschaft und Recht"],
        "UdK_Berlin": ["UdK Berlin", "Universität der Künste"],
        "Charite_Berlin": ["Charité", "Charite Universitätsmedizin"],
        "Alice_Salomon_Hochschule": ["Alice Salomon Hochschule", "ASH Berlin"],
        "KHB_Berlin": ["Kunsthochschule Berlin-Weißensee", "KHB"],
        "Hanns_Eisler": ["Hochschule für Musik Hanns Eisler"],
        "EHB_Berlin": ["Evangelische Hochschule Berlin", "EHB"],
        "KHSB_Berlin": ["Katholische Hochschule für Sozialwesen", "KHSB"],
        "Touro_College": ["Touro College Berlin"],
        "Berlin_International": ["Berlin International University", "BI"],
        "SRH_Berlin": ["SRH Berlin", "SRH Hochschule"],
        "IUBH_IU": ["IUBH", "IU Internationale Hochschule", "IU International University"],
        "Macromedia": ["Macromedia Hochschule"],
        "Mediadesign_Hochschule": ["Mediadesign Hochschule", "MD.H"],
        "Codingschool_Berlin": ["Codingschool Berlin", "Codingschool"],
        "Berlin_School_of_Business": ["Berlin School of Business", "BSB Berlin"],

        # --- B. أهم الجامعات التقنية في ألمانيا (TU9 & Technical) ---
        "RWTH_Aachen": ["RWTH Aachen", "Rheinisch-Westfälische Technische Hochschule"],
        "TUM_Muenchen": ["TU München", "Technische Universität München", "TUM"],
        "KIT_Karlsruhe": ["KIT", "Karlsruher Institut für Technologie"],
        "TU_Dresden": ["TU Dresden", "Technische Universität Dresden"],
        "TU_Darmstadt": ["TU Darmstadt"],
        "Uni_Stuttgart": ["Universität Stuttgart"],
        "TU_Braunschweig": ["TU Braunschweig"],
        "Leibniz_Uni_Hannover": ["Leibniz Universität Hannover"],
        
        # --- C. جامعات الغرب (NRW, Hessen, etc.) ---
        "Uni_Koeln": ["Universität zu Köln", "Uni Köln"],
        "Uni_Bonn": ["Rheinische Friedrich-Wilhelms-Universität Bonn", "Uni Bonn"],
        "Uni_Muenster": ["WWU Münster", "Westfälische Wilhelms-Universität"],
        "Ruhr_Uni_Bochum": ["Ruhr-Universität Bochum", "RUB"],
        "Uni_Duisburg_Essen": ["Universität Duisburg-Essen", "UDE"],
        "Uni_Frankfurt": ["Goethe-Universität Frankfurt", "Uni Frankfurt"],
        "Uni_Mainz": ["Johannes Gutenberg-Universität Mainz"],
        "FernUni_Hagen": ["FernUniversität in Hagen", "FernUni Hagen"], # مهمة جداً للدراسة عن بعد
        "FOM_Hochschule": ["FOM Hochschule", "FOM"],

        # --- D. جامعات الجنوب (Bayern, Bawü) ---
        "LMU_Muenchen": ["LMU München", "Ludwig-Maximilians-Universität"],
        "Uni_Heidelberg": ["Universität Heidelberg", "Ruprecht-Karls-Universität"],
        "Uni_Tuebingen": ["Universität Tübingen", "Eberhard Karls Universität"],
        "Uni_Freiburg": ["Universität Freiburg", "Albert-Ludwigs-Universität"],
        "HM_Muenchen": ["Hochschule München", "HM"],
        "FAU_Erlangen": ["FAU Erlangen-Nürnberg", "Friedrich-Alexander-Universität"],

        # --- E. جامعات الشمال (Hamburg, Bremen, Kiel) ---
        "Uni_Hamburg": ["Universität Hamburg", "UHH"],
        "HAW_Hamburg": ["HAW Hamburg", "Hochschule für Angewandte Wissenschaften Hamburg"],
        "TU_Hamburg": ["TU Hamburg", "TUHH"],
        "Uni_Bremen": ["Universität Bremen"],
        "Uni_Kiel": ["Christian-Albrechts-Universität zu Kiel", "CAU"],

        # --- F. جامعات الشرق (Leipzig, Potsdam, etc.) ---
        "Uni_Leipzig": ["Universität Leipzig"],
        "Uni_Potsdam": ["Universität Potsdam"],
        "Uni_Halle": ["Martin-Luther-Universität Halle-Wittenberg"],
        "Uni_Jena": ["Friedrich-Schiller-Universität Jena"],

        # --- G. منصات ومؤسسات تعليمية عامة ---
        "Uni_Assist": ["uni-assist", "Arbeits- und Servicestelle für internationale Studienbewerbungen"],
        "Hochschulstart": ["Hochschulstart", "Stiftung für Hochschulzulassung"],
        "DAAD": ["DAAD", "Deutscher Akademischer Austauschdienst"],
        "Goethe_Institut": ["Goethe-Institut"],
        "Udemy": ["Udemy"],
        "Coursera": ["Coursera"],
        "EdX": ["edX"],

        # === 🏢 1. Telco & Internet ===
        "Vodafone": ["Vodafone", "Unitymedia", "Kabel Deutschland"],
        "Telekom": ["Telekom", "Magenta", "T-Mobile", "Deutsche Telekom"],
        "O2_Telefonica": ["O2", "Telefónica", "Telefonica"],
        "1und1": ["1&1", "1und1", "Drillisch"],
        "Congstar": ["Congstar"],
        "Blau": ["Blau.de", "Blau Mobilfunk"],
        "Klarmobil": ["Klarmobil"],
        "PYUR": ["PYUR", "Tele Columbus"],
        "WinSIM": ["winSIM"],

# === 💻 2. Electronics & Tech (Top 40 Germany) ===
        "MediaMarkt": ["MediaMarkt", "Media Markt", "MMS E-Commerce"],
        "Saturn": ["Saturn", "Saturn Online"],
        "Amazon": ["Amazon", "Amazon.de", "Amazon EU", "Amazon Payments", "AMZN"],
        "Cyberport": ["Cyberport"],
        "Notebooksbilliger": ["notebooksbilliger.de", "NBB"],
        "Mindfactory": ["Mindfactory", "Mindfactory AG"],
        "Alternate": ["Alternate"],
        "Caseking": ["Caseking", "Caseking GmbH"], # مشهور جداً في برلين للقيمرز
        "Galaxus": ["Galaxus", "Galaxus Deutschland"],
        "ComputerUniverse": ["computeruniverse"],
        "Conrad": ["Conrad Electronic", "Conrad"],
        "Reichelt": ["Reichelt", "Reichelt Elektronik"],
        "Euronics": ["Euronics"],
        "Expert": ["Expert", "Expert Techno"],
        "Gravis": ["Gravis"],
        "Apple": ["Apple", "Apple Store", "iTunes", "Apple Services"],
        "Google": ["Google", "Google Ireland", "Google Play", "Google Cloud"],
        "Microsoft": ["Microsoft", "Microsoft Ireland", "Azure", "Xbox"],
        "Samsung": ["Samsung", "Samsung Electronics"],
        "Sony": ["Sony", "PlayStation"],
        "Nintendo": ["Nintendo"],
        "Adobe": ["Adobe", "Adobe Systems", "Creative Cloud"],
        "Bose": ["Bose"],
        "Teufel": ["Teufel", "Lautsprecher Teufel"], # ماركة صوتيات برلينية
        "Sonos": ["Sonos"],
        "Dyson": ["Dyson"],
        "Vorwerk": ["Vorwerk", "Thermomix"],
        "Rebuy": ["rebuy"],
        "BackMarket": ["Back Market", "BackMarket"],
        "Refurbed": ["Refurbed"],
        "Grover": ["Grover"], # للإيجار
        "Thomann": ["Musikhaus Thomann", "Thomann"], # للموسيقيين
        "MusicStore": ["Music Store"],
        "Calumet_Photo": ["Calumet", "Calumet Photographic"],
        "Foto_Koch": ["Foto Koch"],
        "Medion": ["Medion"],
        "HP_Store": ["HP Store", "HP Deutschland"],
        "Dell": ["Dell", "Dell Technologies"],
        "Lenovo": ["Lenovo"],
        "Logitech": ["Logitech"],

        # === ☁️ 3. Hosting & Dev ===
        "Hetzner": ["Hetzner", "Hetzner Online"],
        "Strato": ["Strato"],
        "Ionos": ["Ionos", "1&1 Ionos"],
        "Hostinger": ["Hostinger"],
        "GitHub": ["GitHub"],
        "JetBrains": ["JetBrains"],
        "Adobe": ["Adobe", "Adobe Systems"],
        "Namecheap": ["Namecheap"],
        "GoDaddy": ["GoDaddy"],

 # === 🛍️ 4. Shopping & Fashion (Top 40 Germany) ===
        "Zalando": ["Zalando", "Zalando SE"],
        "AboutYou": ["About You", "AboutYou"],
        "ASOS": ["ASOS"],
        "OTTO": ["OTTO GmbH", "OTTO"],
        "Galeria": ["Galeria", "Karstadt", "Kaufhof", "Galeria Karstadt Kaufhof"],
        "Breuninger": ["Breuninger"],
        "BestSecret": ["BestSecret"],
        "H_and_M": ["H&M", "Hennes & Mauritz"],
        "Zara": ["Zara", "Inditex"],
        "Mango": ["Mango"],
        "C_and_A": ["C&A", "C und A"],
        "Peek_Cloppenburg": ["Peek & Cloppenburg", "P&C"],
        "Uniqlo": ["Uniqlo"],
        "Primark": ["Primark"],
        "TK_Maxx": ["TK Maxx"],
        "Woolworth": ["Woolworth"],
        "Kik": ["Kik Textilien"],
        "Nike": ["Nike", "Nike Retail"],
        "Adidas": ["Adidas"],
        "Puma": ["Puma"],
        "JD_Sports": ["JD Sports"],
        "Snipes": ["Snipes"],
        "FootLocker": ["Foot Locker"],
        "Deichmann": ["Deichmann"],
        "Decathlon": ["Decathlon"],
        "SportScheck": ["SportScheck"],
        "Intersport": ["Intersport"],
        "IKEA": ["IKEA", "IKEA Deutschland"],
        "Wayfair": ["Wayfair"],
        "Home24": ["Home24"],
        "Westwing": ["Westwing"],
        "Jysk": ["Jysk", "Dänisches Bettenlager"],
        "XXXLLutz": ["XXXLutz", "Mömax"],
        "Höffner": ["Höffner", "Möbel Höffner"],
        "Poco": ["Poco", "Poco Einrichtungsmärkte"],
        "Bauhaus": ["Bauhaus"],
        "Obi": ["Obi", "Obi GmbH"],
        "Hornbach": ["Hornbach"],
        "Toom": ["Toom Baumarkt"],
        "Douglas": ["Douglas"],
        "Sephora": ["Sephora"],
        "Flaconi": ["Flaconi"],
        "Notino": ["Notino"],
        "eBay": ["eBay"],
        "Vinted": ["Vinted"],
        "Kleinanzeigen": ["Kleinanzeigen", "eBay Kleinanzeigen"],
        "Etsy": ["Etsy"],
        "Tchibo": ["Tchibo"],

  # === 🛒 5. Groceries & Drugstores (Top 40 Germany) ===
        "Rewe": ["Rewe", "Rewe Markt", "Rewe Lieferservice"],
        "Edeka": ["Edeka"],
        "Kaufland": ["Kaufland"],
        "Lidl": ["Lidl"],
        "Aldi": ["Aldi Nord", "Aldi Süd", "Aldi"],
        "Netto": ["Netto Marken-Discount", "Netto"],
        "Penny": ["Penny", "Penny Markt"],
        "Norma": ["Norma"],
        "Real": ["Real GmbH", "mein real"],
        "Globus": ["Globus"],
        "Hit_Markt": ["Hit Markt", "Hit Handelsgruppe"],
        "Metro": ["Metro", "Metro Deutschland"], # للجملة
        "DM_Drogerie": ["dm-drogerie", "dm drogerie markt", "dm-markt"],
        "Rossmann": ["Rossmann", "Dirk Rossmann"],
        "Mueller": ["Müller Handels", "Müller Drogerie"],
        "Budni": ["Budni", "Budnikowsky"],
        "Bio_Company": ["Bio Company"], # مشهور جداً في برلين
        "Denns_Bio": ["Denns", "Denn's Biomarkt"],
        "Alnatura": ["Alnatura"],
        "Reformhaus": ["Reformhaus"],
        "Flaschenpost": ["Flaschenpost"],
        "Picnic": ["Picnic"],
        "Knuspr": ["Knuspr"],
        "HelloFresh": ["HelloFresh"],
        "MarleySpoon": ["Marley Spoon"],
        "Lieferando": ["Lieferando", "Takeaway.com"],
        "Wolt": ["Wolt"],
        "UberEats": ["Uber Eats"],
        "Fressnapf": ["Fressnapf"], # للحيوانات الأليفة
        "Zooplus": ["Zooplus"],
        "Das_Futterhaus": ["Das Futterhaus"],
        "Shop_Apotheke": ["Shop Apotheke", "Redcare Pharmacy"],
        "DocMorris": ["DocMorris"],
        "Medpex": ["Medpex"],
        "Apotheke": ["Apotheke"], # صيدليات عامة
        "Douglas": ["Douglas"],
        "Rituals": ["Rituals"],
        "Nespresso": ["Nespresso"],

        # === 💶 6. Banking & Fintech ===
        "Sparkasse": ["Sparkasse", "Berliner Sparkasse"],
        "Volksbank": ["Volksbank", "Raiffeisenbank"],
        "Deutsche_Bank": ["Deutsche Bank"],
        "Commerzbank": ["Commerzbank"],
        "Postbank": ["Postbank"],
        "ING_DiBa": ["ING", "ING-DiBa"],
        "DKB": ["DKB", "Deutsche Kreditbank"],
        "N26": ["N26", "N26 Bank"],
        "TradeRepublic": ["Trade Republic"],
        "Comdirect": ["comdirect"],
        "PayPal": ["PayPal"],
        "Klarna": ["Klarna"],
        "Visa_Mastercard": ["Visa", "Mastercard"],
        "Schufa": ["Schufa", "Schufa Holding"],
        "Revolut": ["Revolut"],
        "Wise": ["Wise", "TransferWise"],

        # === 🏥 7. Insurance & Health ===
        "TK_Krankenkasse": ["Techniker Krankenkasse", "Die TK"],
        "AOK": ["AOK", "AOK Nordost", "AOK Plus"],
        "Barmer": ["Barmer"],
        "DAK": ["DAK-Gesundheit"],
        "Allianz": ["Allianz"],
        "AXA": ["AXA"],
        "HUK_Coburg": ["HUK-COBURG", "HUK24"],
        "Ergo": ["ERGO"],
        "Debeka": ["Debeka"],
        "Generali": ["Generali"],
        "Doctolib": ["Doctolib"],

        # === 🏠 8. Housing & Energy ===
        "Vattenfall": ["Vattenfall"],
        "EON": ["E.ON", "E.ON Energie"],
        "GASAG": ["GASAG"],
        "EnBW": ["EnBW"],
        "RWE": ["RWE"],
        "Stadtwerke": ["Stadtwerke"],
        "Vonovia": ["Vonovia"],
        "Deutsche_Wohnen": ["Deutsche Wohnen"],
        "Mietvertrag": ["Mietvertrag", "Vermieter", "Hausverwaltung"],

        # === 🚅 9. Transport & Travel ===
        "Deutsche_Bahn": ["Deutsche Bahn", "DB Vertrieb", "DB Fernverkehr"],
        "BVG_Berlin": ["BVG", "Berliner Verkehrsbetriebe"],
        "S_Bahn": ["S-Bahn"],
        "Lufthansa": ["Lufthansa"],
        "Ryanair": ["Ryanair"],
        "Eurowings": ["Eurowings"],
        "FlixBus": ["FlixBus", "FlixTrain"],
        "Uber": ["Uber"],
        "Bolt": ["Bolt"],
        "ShareNow": ["Share Now", "Car2Go"],
        "Miles": ["Miles Mobility"],
        "Sixt": ["Sixt"],
        "Booking": ["Booking.com"],
        "Airbnb": ["Airbnb"],

        # === 🎬 10. Subscriptions ===
        "Netflix": ["Netflix"],
        "Spotify": ["Spotify"],
        "Disney_Plus": ["Disney+"],
        "DAZN": ["DAZN"],
        "Sky": ["Sky Deutschland", "WOW"],
        "McFit": ["McFit", "RSG Group"],
        "FitX": ["FitX"],
        "Check24": ["CHECK24", "Tarifdetektiv"],
        "YouTube": ["YouTube", "Google LLC"],

        # === 📦 11. Delivery ===
        "DHL": ["DHL", "Deutsche Post"],
        "Hermes": ["Hermes", "Hermes Germany"],
        "DPD": ["DPD"],
        "UPS": ["UPS"],
        "Lieferando": ["Lieferando"],
        "Wolt": ["Wolt"],
        "UberEats": ["Uber Eats"],

# === 🏛️ 12. Government & Official (Top German Bureaucracy) ===
        "Finanzamt": ["Finanzamt", "Steuerbescheid", "Einkommensteuer", "Lohnsteuer", "Elster"],
        "Bundeszentralamt_Steuern": ["Bundeszentralamt für Steuern", "BZSt", "Steuer-ID"],
        "Jobcenter": ["Jobcenter", "Arbeitslosengeld", "Bürgergeld"],
        "Bundesagentur_fuer_Arbeit": ["Bundesagentur für Arbeit", "Arbeitsagentur", "Arbeitsamt"],
        "Familienkasse": ["Familienkasse", "Kindergeld", "Kinderzuschlag"],
        "Rentenversicherung": ["Deutsche Rentenversicherung", "DRV", "Sozialversicherungsausweis", "Renteninformation"],
        
        # --- Immigration & Residency (Important for Expats) ---
        "LEA_Auslaenderbehoerde": ["Landesamt für Einwanderung", "LEA", "Ausländerbehörde", "Aufenthaltstitel", "Fiktionsbescheinigung"],
        "Buergeramt": ["Bürgeramt", "Einwohnermeldeamt", "Meldebescheinigung", "Wohnungsgeberbestätigung", "Bürgerbüro"],
        "Standesamt": ["Standesamt", "Geburtsurkunde", "Eheurkunde", "Sterbeurkunde"],
        "Einbuergerung": ["Einbürgerungsbehörde", "Staatsangehörigkeit"],
        
        # --- Student & Housing Support ---
        "BAfoeG_Amt": ["BAföG", "Amt für Ausbildungsförderung", "Studierendenwerk", "Bafög-Bescheid"],
        "Wohngeldstelle": ["Wohngeldstelle", "Wohngeld", "Mietzuschuss"],
        "Wohnberechtigungsschein": ["Wohnberechtigungsschein", "WBS"],
        
        # --- Legal & Police ---
        "Polizei": ["Polizei", "Bußgeldbescheid", "Anhörungsbogen", "Landeskriminalamt", "LKA"],
        "Amtsgericht": ["Amtsgericht", "Landgericht", "Staatsanwaltschaft", "Urteil", "Mahnbescheid"],
        "Zoll": ["Zoll", "Hauptzollamt", "Einfuhrabgaben"],
        
        # --- Vehicle & Transport Official ---
        "Kfz_Zulassung": ["Kfz-Zulassungsstelle", "Zulassungsbescheinigung", "Fahrzeugschein"],
        "Fuehrerscheinstelle": ["Führerscheinstelle", "Fahrerlaubnisbehörde"],
        "TUEV_Dekra": ["TÜV", "DEKRA", "Hauptuntersuchung"], # شبه رسمي
        
        # --- Other Official Bodies ---
        "Rundfunkbeitrag": ["Rundfunkbeitrag", "ARD ZDF Deutschlandradio", "Beitragsservice", "GEZ"],
        "Gesundheitsamt": ["Gesundheitsamt", "Infektionsschutzbelehrung"],
        "IHK": ["IHK", "Industrie- und Handelskammer"], # للفريلانسر والشركات
        "Handwerkskammer": ["Handwerkskammer", "HWK"],
        "Schufa": ["Schufa", "Schufa Holding", "Bonitätsauskunft"], # ليست حكومية ولكن تعامل معاملة الرسمي
        "Deutsche_Post_E_Post": ["Deutsche Post", "E-Post"], # للرسائل المسجلة Einschreiben
    }

        
        months = {
            "01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr",
            "05": "May", "06": "Jun", "07": "Jul", "08": "Aug",
            "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"
        }

        processed_count = 0
        errors_count = 0

        files = [f for f in os.listdir(folder_path) if f.lower().endswith(".pdf") and len(f) > 5]
        
        if len(files) == 0:
             self.log("⚠️ لا توجد ملفات PDF في هذا المجلد")
             self.finish_process()
             return

        for filename in files:
            self.log(f"جارٍ فحص: {filename}")
            file_path = os.path.join(folder_path, filename)
            
            try:
                with pdfplumber.open(file_path) as pdf:
                    if not pdf.pages:
                        continue
                    first_page_text = pdf.pages[0].extract_text()
                    if not first_page_text: continue 

                    # تحديد المرسل
                    found_sender = "Other_Docs"
                    for sender, keywords in senders_keywords.items():
                        if any(k.lower() in first_page_text.lower() for k in keywords):
                            found_sender = sender
                            break
                    
                    # المنطق
                    semester_info = ""
                    doc_type = ""
                    final_date_part = ""
                    is_uni = any(uni_hint in found_sender for uni_hint in ["Berlin", "Hochschule", "University", "Uni_Assist"])
                    
                    if is_uni:
                        wise_match = re.search(r'(Wintersemester|WiSe)[^\d]*(\d{4})[/-]?(\d{2,4})?', first_page_text, re.IGNORECASE)
                        sose_match = re.search(r'(Sommersemester|SoSe)[^\d]*(\d{4})', first_page_text, re.IGNORECASE)
                        if wise_match:
                            year_suffix = f"-{wise_match.group(3)[-2:]}" if wise_match.group(3) else ""
                            semester_info = f"WiSe_{wise_match.group(2)}{year_suffix}"
                        elif sose_match:
                            semester_info = f"SoSe_{sose_match.group(2)}"

                        if "Immatrikulation" in first_page_text: doc_type = "_Immatrikulation"
                        elif "Bescheinigung" in first_page_text: doc_type = "_Bescheinigung"
                        elif "Notenübersicht" in first_page_text: doc_type = "_Noten"
                        elif "Zulassungsbescheid" in first_page_text: doc_type = "_Zulassung"
                    
                    if not semester_info:
                        date_match = re.search(r'(\d{2})\.(\d{2})\.(\d{4})', first_page_text)
                        if "Rechnung" in first_page_text: doc_type = "_Rechnung"
                        elif "Mahnung" in first_page_text: doc_type = "_Mahnung"
                        elif "Vertrag" in first_page_text: doc_type = "_Vertrag"

                        if date_match:
                            month_name = months.get(date_match.group(2), date_match.group(2))
                            final_date_part = f"{month_name}_{date_match.group(3)}"
                        else:
                            year_match = re.search(r'20\d{2}', first_page_text)
                            final_date_part = year_match.group(0) if year_match else "General"

                    if semester_info:
                        new_name = f"{found_sender}_{semester_info}{doc_type}.pdf"
                    else:
                        new_name = f"{found_sender}_{final_date_part}{doc_type}.pdf" if doc_type or final_date_part != "General" else f"{found_sender}_{filename}"

                    pdf.close()

                    # النقل
                    target_folder = os.path.join(folder_path, found_sender)
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)

                    new_file_path = os.path.join(target_folder, new_name)
                    counter = 1
                    base_name = new_name.replace(".pdf", "")
                    while os.path.exists(new_file_path):
                        new_file_path = os.path.join(target_folder, f"{base_name}_{counter}.pdf")
                        counter += 1

                    os.rename(file_path, new_file_path)
                    self.log(f"✅ تم النقل: {found_sender}")
                    processed_count += 1
            
            except Exception as e:
                self.log(f"❌ خطأ: {e}")
                errors_count += 1

        self.finish_process(processed_count, errors_count)

    def finish_process(self, processed=0, errors=0):
        self.progressbar.stop()
        self.progressbar.set(1)
        self.log("========================================")
        self.log(f"✨ تمت العملية بنجاح! تم نقل {processed} ملفات")
        self.btn_start.configure(state="normal")

if __name__ == "__main__":
    app = InvoiceOrganizerApp()
    app.mainloop()