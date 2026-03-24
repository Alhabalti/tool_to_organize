import { Request, Response } from 'express';

class UserController {
    public async getUsers(req: Request, res: Response): Promise<void> {
        // Logic to retrieve users
        res.send('List of users');
    }

    public async getUserById(req: Request, res: Response): Promise<void> {
        const userId = req.params.id;
        // Logic to retrieve a user by ID
        res.send(`User with ID: ${userId}`);
    }

    public async createUser(req: Request, res: Response): Promise<void> {
        const userData = req.body;
        // Logic to create a new user
        res.status(201).send('User created');
    }
}

class ProductController {
    public async getProducts(req: Request, res: Response): Promise<void> {
        // Logic to retrieve products
        res.send('List of products');
    }

    public async getProductById(req: Request, res: Response): Promise<void> {
        const productId = req.params.id;
        // Logic to retrieve a product by ID
        res.send(`Product with ID: ${productId}`);
    }

    public async createProduct(req: Request, res: Response): Promise<void> {
        const productData = req.body;
        // Logic to create a new product
        res.status(201).send('Product created');
    }
}

export { UserController, ProductController };