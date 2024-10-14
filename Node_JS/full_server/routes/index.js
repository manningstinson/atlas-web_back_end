import { Router } from 'express';
import AppController from '../controllers/AppController.js';
import StudentsController from '../controllers/StudentsController.js';

const router = Router();

// Link the root ("/") route to the AppController
router.get('/', AppController.getHomepage);

// Link the "/students" route to the StudentsController
router.get('/students', StudentsController.getAllStudents);

// Link the "/students/:major" route to the StudentsController
router.get('/students/:major', StudentsController.getAllStudentsByMajor);

export default router;
