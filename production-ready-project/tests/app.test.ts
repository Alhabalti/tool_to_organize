import request from 'supertest';
import app from '../src/app'; // Adjust the path if necessary

describe('App Routes', () => {
    it('should return 200 for the root route', async () => {
        const response = await request(app).get('/');
        expect(response.status).toBe(200);
    });

    // Add more tests for other routes and controllers as needed
});