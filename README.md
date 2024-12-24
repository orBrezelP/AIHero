#AI Heroes Recipie project#
---

### Steps to Run the Application

#### 1. **Start Backend with Docker Compose**
   - Ensure you have Docker and Docker Compose installed on your system.
   - Navigate to the directory containing the `docker-compose.yml` file.
   - Run the following command:
     ```bash
     docker-compose up -d
     ```
   - This will start the backend services defined in the `docker-compose.yml` file in detached mode.

#### 2. **Add OpenAI Key**
   - Navigate to the `src` folder in your frontend directory:
     ```bash
     cd src
     ```
   - Open the `.env` file (create it if it doesn’t exist).
   - Add your OpenAI key in the following format:
     ```env
     OPENAI_API_KEY=your-openai-api-key
     ```
   - Save the file.

#### 3. **Install Frontend Dependencies**
   - Ensure you have [PNPM](https://pnpm.io/) installed.
   - Navigate to the frontend directory:
     ```bash
     cd path/to/frontend
     ```
   - Install the dependencies:
     ```bash
     pnpm i
     ```

#### 4. **Run Frontend**
   - Start the frontend development server:
     ```bash
     pnpm start
     ```
   - This will typically start the frontend on a development server, often accessible at `http://localhost:3000` or a similar port.

#### 5. **Verify Application**
   - Check if both the backend and frontend are running correctly.
   - Open your browser and navigate to the frontend URL, or use a tool like Postman to test the backend API.

---

Let me know if you need help with anything else!
