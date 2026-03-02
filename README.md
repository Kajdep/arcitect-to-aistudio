# The Arrcitect

A premium full-stack Next.js application that transforms high-level project briefs into technical, conversion-optimized blueprints for Carrd.co.

## Features

- **Architectural Dark Mode:** Premium UI with Deep Charcoal, Slate, and Neon-Blue accents.
- **AI-Powered Blueprints:** Integrates with Gemini 2.0 Flash (`@google/genai`) to generate structured design systems, structural scaffolding, copywriting, and custom code blocks.
- **Local Grounding:** Uses a local Knowledge Base (text files inside `/knowledge`) to ensure recommendations strictly follow the capabilities documented.

## Getting Started

### 1. Configure the Knowledge Base
To give the AI the proper context, you MUST place your Carrd.co knowledge base files into the newly created `/knowledge` directory in the project root.
- Move all `.txt` documents from `D:\arrcitect\Carrd_Knowledge_Base` into `D:\arrcitect\knowledge`.

### 2. Configure Environment Variables
Copy the example environment file and add your Google Gemini API key:
```bash
cp .env.example .env.local
```
Open `.env.local` and set your `GEMINI_API_KEY`.

### 3. Run the Development Server
Install dependencies (if not already done) and start the server:
```bash
npm install
npm run dev
```
Open [http://localhost:3000](http://localhost:3000) in your browser.
