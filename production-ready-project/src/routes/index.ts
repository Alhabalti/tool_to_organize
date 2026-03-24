import { Router } from 'express';
import { UserController } from '../controllers/index';
import { ProductController } from '../controllers/index';

const router = Router();

export const setRoutes = () => {
    // User routes
    router.get('/users', UserController.getAllUsers);
    router.post('/users', UserController.createUser);
    router.get('/users/:id', UserController.getUserById);
    router.put('/users/:id', UserController.updateUser);
    router.delete('/users/:id', UserController.deleteUser);

    // Product routes
    router.get('/products', ProductController.getAllProducts);
    router.post('/products', ProductController.createProduct);
    router.get('/products/:id', ProductController.getProductById);
    router.put('/products/:id', ProductController.updateProduct);
    router.delete('/products/:id', ProductController.deleteProduct);

    return router;
};