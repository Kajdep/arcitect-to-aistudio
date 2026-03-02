import { getKnowledgeBaseContext } from '@/lib/knowledge-base';
import { NextResponse } from 'next/server';
import { GoogleGenAI, Type } from '@google/genai';

// Initialize the Gemini client using the environment variable
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

export async function POST(req: Request) {
    try {
        const { brief } = await req.json();

        if (!brief) {
            return NextResponse.json({ error: 'Brief is required' }, { status: 400 });
        }

        const contextContext = getKnowledgeBaseContext();

        const systemInstruction = `You are The Arrcitect, an elite strategist for the Carrd.co platform. Your mission is to architect high-ticket, high-converting one-page websites.

Strict Fidelity: Use ONLY the technical capabilities and 'hacks' (CSS snippets, container settings, section breaks) found in the provided Knowledge Base.

Anti-Hallucination: If a feature isn't in the documents, state it requires an external integration (e.g., Outseta for memberships).

Design Excellence: Recommend specific font pairings and HEX codes directly from the design docs.

Conversion Logic: Write persuasive headlines and CTAs based on the 'Conversion Framework' in the strategy docs.

Output Requirement: You are a headless API. You must respond ONLY with valid JSON matching the provided schema.

KNOWLEDGE BASE:
${contextContext}`;

        const schema = {
            type: Type.OBJECT,
            properties: {
                design: {
                    type: Type.OBJECT,
                    properties: {
                        theme_vibe: { type: Type.STRING },
                        background_color: { type: Type.STRING },
                        primary_font: { type: Type.STRING },
                        secondary_font: { type: Type.STRING },
                        accent_colors: { type: Type.ARRAY, items: { type: Type.STRING } }
                    },
                    required: ["theme_vibe", "background_color", "primary_font", "secondary_font", "accent_colors"]
                },
                structure: {
                    type: Type.ARRAY,
                    items: {
                        type: Type.OBJECT,
                        properties: {
                            section_name: { type: Type.STRING },
                            container_settings: { type: Type.STRING },
                            elements_to_add: { type: Type.ARRAY, items: { type: Type.STRING } }
                        },
                        required: ["section_name", "container_settings", "elements_to_add"]
                    }
                },
                copy: {
                    type: Type.OBJECT,
                    properties: {
                        hero_h1: { type: Type.STRING },
                        hero_subheadline: { type: Type.STRING },
                        primary_cta: { type: Type.STRING },
                        feature_bullets: { type: Type.ARRAY, items: { type: Type.STRING } }
                    },
                    required: ["hero_h1", "hero_subheadline", "primary_cta", "feature_bullets"]
                },
                code: {
                    type: Type.ARRAY,
                    items: {
                        type: Type.OBJECT,
                        properties: {
                            plugin_name: { type: Type.STRING },
                            instructions: { type: Type.STRING },
                            code_snippet: { type: Type.STRING }
                        },
                        required: ["plugin_name", "instructions", "code_snippet"]
                    }
                }
            },
            required: ["design", "structure", "copy", "code"]
        };

        const response = await ai.models.generateContent({
            model: 'gemini-3.1-pro-preview',
            contents: brief,
            config: {
                systemInstruction: systemInstruction,
                responseMimeType: 'application/json',
                responseSchema: schema,
            }
        });

        const outputText = response.text;
        if (!outputText) {
            throw new Error('No response text generated.');
        }

        return NextResponse.json(JSON.parse(outputText));

    } catch (error: any) {
        console.error('API Error:', error);
        return NextResponse.json({ error: error.message }, { status: 500 });
    }
}
