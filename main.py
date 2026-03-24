import os
import re
import pdfplumber
import traceback

def organize_files_mega_english():
    # Current working directory
    folder_path = os.getcwd()
    
    print("\n" + "="*60)
    print("🚀 Starting Ultimate Archiver (Abdullah's Pro Edition)")
    print("="*60)

    # --- 📚 Full Dictionary (Mega Archive) ---
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

    # Iterate over files
    for filename in os.listdir(folder_path):
        # Filter files (PDF only, length > 5)
        if filename.lower().endswith(".pdf") and len(filename) > 5:
            file_path = os.path.join(folder_path, filename)
            
            try:
                # Open PDF
                with pdfplumber.open(file_path) as pdf:
                    if not pdf.pages:
                        print(f"⚠️ Empty file: {filename}")
                        continue
                        
                    first_page_text = pdf.pages[0].extract_text()
                    if not first_page_text: 
                        continue 

                    # 1. Identify Sender
                    found_sender = "Other_Docs"
                    for sender, keywords in senders_keywords.items():
                        if any(k.lower() in first_page_text.lower() for k in keywords):
                            found_sender = sender
                            break
                    
                    # Variables for renaming
                    semester_info = ""
                    doc_type = ""
                    final_date_part = ""

                    # === University Logic ===
                    is_uni = any(uni_hint in found_sender for uni_hint in ["Berlin", "Hochschule", "University", "School", "Uni_Assist"])
                    
                    if is_uni:
                        # Regex for Semester (WiSe/SoSe)
                        wise_match = re.search(r'(Wintersemester|WiSe)[^\d]*(\d{4})[/-]?(\d{2,4})?', first_page_text, re.IGNORECASE)
                        sose_match = re.search(r'(Sommersemester|SoSe)[^\d]*(\d{4})', first_page_text, re.IGNORECASE)

                        if wise_match:
                            year1 = wise_match.group(2)
                            year2 = wise_match.group(3)
                            year_suffix = f"-{year2[-2:]}" if year2 else ""
                            semester_info = f"WiSe_{year1}{year_suffix}"
                        
                        elif sose_match:
                            semester_info = f"SoSe_{sose_match.group(2)}"

                        # Doc Types
                        if "Immatrikulation" in first_page_text: doc_type = "_Immatrikulation"
                        elif "Bescheinigung" in first_page_text: doc_type = "_Bescheinigung"
                        elif "Notenübersicht" in first_page_text or "Leistungsübersicht" in first_page_text: doc_type = "_Noten"
                        elif "Exmatrikulation" in first_page_text: doc_type = "_Exmatrikulation"
                        elif "Zulassungsbescheid" in first_page_text: doc_type = "_Zulassung"
                    
                    # === Company/Invoice Logic ===
                    if not semester_info:
                        # Date Regex dd.mm.yyyy
                        date_match = re.search(r'(\d{2})\.(\d{2})\.(\d{4})', first_page_text)
                        
                        # Invoice Types
                        if "Mahnung" in first_page_text: doc_type = "_Mahnung"
                        elif "Gutschrift" in first_page_text: doc_type = "_Gutschrift"
                        elif "Rechnung" in first_page_text: doc_type = "_Rechnung"
                        elif "Vertrag" in first_page_text: doc_type = "_Vertrag"
                        elif "Kündigung" in first_page_text: doc_type = "_Kündigung"

                        if date_match:
                            month_name = months.get(date_match.group(2), date_match.group(2))
                            year = date_match.group(3)
                            final_date_part = f"{month_name}_{year}"
                        else:
                            # Fallback to year only
                            year_match = re.search(r'20\d{2}', first_page_text)
                            year = year_match.group(0) if year_match else "General"
                            final_date_part = f"{year}"

                    # === Construct New Name ===
                    if semester_info:
                        new_name = f"{found_sender}_{semester_info}{doc_type}.pdf"
                    else:
                        if not doc_type and final_date_part == "General":
                             new_name = f"{found_sender}_{filename}"
                        else:
                             new_name = f"{found_sender}_{final_date_part}{doc_type}.pdf"

                    pdf.close()

                    # Create Folder
                    target_folder = os.path.join(folder_path, found_sender)
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)

                    # Move File (Handle Duplicates)
                    new_file_path = os.path.join(target_folder, new_name)
                    
                    counter = 1
                    base_name = new_name.replace(".pdf", "")
                    while os.path.exists(new_file_path):
                        new_file_path = os.path.join(target_folder, f"{base_name}_{counter}.pdf")
                        counter += 1

                    os.rename(file_path, new_file_path)
                    print(f"✅ Moved: {new_name}")
                    processed_count += 1
            
            except Exception as e:
                print(f"⚠️ Skipped file {filename}: {str(e)}")
                errors_count += 1

    print("\n" + "="*60)
    print(f"✨ Finished successfully!")
    print(f"📂 Processed files: {processed_count}")
    print(f"❌ Skipped errors: {errors_count}")
    print("="*60)

if __name__ == "__main__":
    try:
        organize_files_mega_english()
    except Exception as e:
        print("\n❌ Critical Error:")
        traceback.print_exc()
    
    input("\nPress Enter to exit...")