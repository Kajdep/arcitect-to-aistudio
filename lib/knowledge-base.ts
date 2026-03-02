import fs from 'fs';
import path from 'path';

export function getKnowledgeBaseContext(): string {
    const knowledgeDir = path.join(process.cwd(), 'knowledge');
    let context = '';

    try {
        if (!fs.existsSync(knowledgeDir)) {
            console.warn('Knowledge directory not found at', knowledgeDir);
            return context;
        }

        const files = fs.readdirSync(knowledgeDir);

        for (const file of files) {
            if (file.endsWith('.txt')) {
                const filePath = path.join(knowledgeDir, file);
                const content = fs.readFileSync(filePath, 'utf-8');
                context += `\n--- SOURCE: ${file} ---\n${content}\n`;
            }
        }
    } catch (error) {
        console.error('Error reading knowledge base:', error);
    }

    return context;
}
