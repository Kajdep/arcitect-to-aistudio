"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Copy, Layers, Type, FileCode2, Sparkles, CheckCircle2, ChevronRight, Hexagon, Loader2 } from "lucide-react";

type Blueprint = {
  design: {
    theme_vibe: string;
    background_color: string;
    primary_font: string;
    secondary_font: string;
    accent_colors: string[];
  };
  structure: {
    section_name: string;
    container_settings: string;
    elements_to_add: string[];
  }[];
  copy: {
    hero_h1: string;
    hero_subheadline: string;
    primary_cta: string;
    feature_bullets: string[];
  };
  code: {
    plugin_name: string;
    instructions: string;
    code_snippet: string;
  }[];
};

export default function ArrcitectDashboard() {
  const [brief, setBrief] = useState("");
  const [isGenerating, setIsGenerating] = useState(false);
  const [blueprint, setBlueprint] = useState<Blueprint | null>(null);
  const [activeTab, setActiveTab] = useState<"design" | "structure" | "copy" | "code">("design");
  const [copiedIndex, setCopiedIndex] = useState<string | null>(null);

  const handleGenerate = async () => {
    if (!brief.trim()) return;
    setIsGenerating(true);
    setBlueprint(null);

    try {
      const response = await fetch("/api/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ brief }),
      });

      if (!response.ok) {
        throw new Error("Failed to generate blueprint");
      }

      const data = await response.json();
      setBlueprint(data);
    } catch (error) {
      console.error(error);
      alert("Error generating blueprint. Make sure your local knowledge base is set up and Gemini API key is configured.");
    } finally {
      setIsGenerating(false);
    }
  };

  const copyToClipboard = (text: string, id: string) => {
    navigator.clipboard.writeText(text);
    setCopiedIndex(id);
    setTimeout(() => setCopiedIndex(null), 2000);
  };

  return (
    <div className="min-h-screen bg-charcoal-900 text-slate-300 font-sans flex flex-col md:flex-row overflow-hidden">
      {/* Left Panel: The Intake */}
      <div className="w-full md:w-5/12 border-b md:border-b-0 md:border-r border-charcoal-700 bg-charcoal-900/50 flex flex-col h-screen overflow-y-auto">
        <div className="p-8 flex items-center space-x-3 border-b border-charcoal-700">
          <div className="w-10 h-10 bg-neon-blue/10 rounded-xl flex items-center justify-center border border-neon-blue/30 shadow-[0_0_15px_rgba(0,240,255,0.2)]">
            <Hexagon className="text-neon-blue w-6 h-6" />
          </div>
          <div>
            <h1 className="text-2xl font-bold text-white tracking-tight">The Arrcitect</h1>
            <p className="text-xs text-neon-blue/70 uppercase tracking-widest font-semibold mt-0.5">Master Blueprint Engine</p>
          </div>
        </div>

        <div className="p-8 flex-1 flex flex-col">
          <label className="text-sm font-semibold text-slate-400 mb-3 uppercase tracking-wider flex items-center">
            Client Project Brief
          </label>
          <textarea
            value={brief}
            onChange={(e) => setBrief(e.target.value)}
            placeholder="Describe the project... E.g., 'A high-ticket coaching funnel for real estate agents. Needs a modern, trustworthy vibe with strong contrast.'"
            className="flex-1 w-full bg-charcoal-800/50 border border-charcoal-700 rounded-xl p-5 text-slate-200 placeholder:text-charcoal-600 focus:outline-none focus:ring-2 focus:ring-neon-blue/50 focus:border-transparent transition-all resize-none shadow-inner"
          />

          <button
            onClick={handleGenerate}
            disabled={isGenerating || !brief.trim()}
            className="mt-6 w-full group relative overflow-hidden rounded-xl bg-neon-blue/10 border border-neon-blue/30 text-neon-blue font-semibold px-6 py-4 transition-all hover:bg-neon-blue/20 hover:shadow-[0_0_20px_rgba(0,240,255,0.2)] disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <div className="flex items-center justify-center space-x-2">
              {isGenerating ? (
                <>
                  <Loader2 className="w-5 h-5 animate-spin" />
                  <span>Drafting Blueprint...</span>
                </>
              ) : (
                <>
                  <Sparkles className="w-5 h-5" />
                  <span>Generate Blueprint</span>
                </>
              )}
            </div>
            {isGenerating && (
              <motion.div
                className="absolute bottom-0 left-0 h-1 bg-neon-blue"
                initial={{ width: "0%" }}
                animate={{ width: "100%" }}
                transition={{ duration: 3, repeat: Infinity, ease: "linear" }}
              />
            )}
          </button>
        </div>
      </div>

      {/* Right Panel: The Output */}
      <div className="w-full md:w-7/12 bg-charcoal-900 flex flex-col h-screen overflow-hidden">
        {!blueprint && !isGenerating ? (
          <div className="flex-1 flex flex-col items-center justify-center p-12 text-center opacity-40">
            <Hexagon className="w-24 h-24 text-charcoal-700 mb-6 stroke-[1]" />
            <h3 className="text-2xl font-light text-slate-500 mb-2">Awaiting Project Data</h3>
            <p className="max-w-md text-sm">Enter a brief in the intake panel to initialize the Arrcitect blueprint generation sequence.</p>
          </div>
        ) : isGenerating ? (
          <div className="flex-1 flex flex-col items-center justify-center p-12">
            <div className="relative w-32 h-32 mb-8">
              <motion.div
                animate={{ rotate: 360 }}
                transition={{ duration: 8, repeat: Infinity, ease: "linear" }}
                className="absolute inset-0 border-2 border-dashed border-neon-blue/30 rounded-full"
              />
              <motion.div
                animate={{ rotate: -360 }}
                transition={{ duration: 12, repeat: Infinity, ease: "linear" }}
                className="absolute inset-4 border-2 border-charcoal-700 rounded-full"
              />
              <div className="absolute inset-0 flex items-center justify-center text-neon-blue">
                <Hexagon className="w-8 h-8 opacity-50" />
              </div>
            </div>
            <h3 className="text-xl font-medium text-white mb-2 tracking-wide font-mono animate-pulse">ANALYZING PARAMETERS</h3>
            <p className="text-slate-500 text-sm">Cross-referencing Carrd knowledge base...</p>
          </div>
        ) : blueprint ? (
          <div className="flex flex-col h-full">
            {/* Tabs */}
            <div className="flex items-end px-6 pt-6 border-b border-charcoal-700 shrink-0 space-x-1">
              {[
                { id: "design", label: "Visual Identity", icon: <Type className="w-4 h-4" /> },
                { id: "structure", label: "Framework", icon: <Layers className="w-4 h-4" /> },
                { id: "copy", label: "Copywriting", icon: <Sparkles className="w-4 h-4" /> },
                { id: "code", label: "Structural Code", icon: <FileCode2 className="w-4 h-4" /> },
              ].map((tab) => (
                <button
                  key={tab.id}
                  onClick={() => setActiveTab(tab.id as any)}
                  className={`flex items-center space-x-2 px-5 py-3 rounded-t-lg transition-all border-b-2 font-medium text-sm ${activeTab === tab.id
                      ? "bg-charcoal-800 text-neon-blue border-neon-blue"
                      : "bg-transparent text-slate-500 border-transparent hover:text-slate-300 hover:bg-charcoal-800/50"
                    }`}
                >
                  {tab.icon}
                  <span>{tab.label}</span>
                </button>
              ))}
            </div>

            {/* Tab Content */}
            <div className="flex-1 overflow-y-auto p-8 relative">
              <AnimatePresence mode="wait">
                <motion.div
                  key={activeTab}
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, y: -10 }}
                  transition={{ duration: 0.2 }}
                  className="space-y-8"
                >
                  {/* DESIGN TAB */}
                  {activeTab === "design" && (
                    <div className="space-y-8">
                      <div>
                        <h3 className="text-lg font-bold text-white mb-4 flex items-center"><ChevronRight className="w-5 h-5 text-neon-blue mr-1" /> Design System</h3>
                        <p className="text-slate-400 bg-charcoal-800/50 p-4 rounded-lg border border-charcoal-700 text-sm leading-relaxed">
                          {blueprint.design.theme_vibe}
                        </p>
                      </div>

                      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div className="bg-charcoal-800/30 p-5 rounded-xl border border-charcoal-700">
                          <p className="text-xs uppercase text-slate-500 mb-3 font-semibold tracking-wider">Typography</p>
                          <div className="space-y-4">
                            <div>
                              <p className="text-white font-medium">{blueprint.design.primary_font}</p>
                              <p className="text-xs text-slate-500 mt-1">Primary Display</p>
                            </div>
                            <div>
                              <p className="text-slate-300 font-medium">{blueprint.design.secondary_font}</p>
                              <p className="text-xs text-slate-500 mt-1">Secondary / Body Text</p>
                            </div>
                          </div>
                        </div>

                        <div className="bg-charcoal-800/30 p-5 rounded-xl border border-charcoal-700">
                          <p className="text-xs uppercase text-slate-500 mb-3 font-semibold tracking-wider">Color Palette</p>
                          <div className="space-y-3">
                            <div className="flex items-center justify-between group cursor-pointer" onClick={() => copyToClipboard(blueprint.design.background_color, 'bg')}>
                              <div className="flex items-center space-x-3">
                                <div className="w-8 h-8 rounded-full border border-charcoal-600 shadow-inner" style={{ backgroundColor: blueprint.design.background_color }}></div>
                                <span className="font-mono text-sm">{blueprint.design.background_color}</span>
                              </div>
                              <span className="text-xs text-slate-500">Base</span>
                              {copiedIndex === 'bg' ? <CheckCircle2 className="w-4 h-4 text-green-400" /> : <Copy className="w-4 h-4 text-slate-600 group-hover:text-neon-blue transition-colors" />}
                            </div>

                            {blueprint.design.accent_colors.map((color, i) => (
                              <div key={i} className="flex items-center justify-between group cursor-pointer" onClick={() => copyToClipboard(color, `accent-${i}`)}>
                                <div className="flex items-center space-x-3">
                                  <div className="w-8 h-8 rounded-full border border-charcoal-600 shadow-inner" style={{ backgroundColor: color }}></div>
                                  <span className="font-mono text-sm">{color}</span>
                                </div>
                                <span className="text-xs text-slate-500">Accent {i + 1}</span>
                                {copiedIndex === `accent-${i}` ? <CheckCircle2 className="w-4 h-4 text-green-400" /> : <Copy className="w-4 h-4 text-slate-600 group-hover:text-neon-blue transition-colors" />}
                              </div>
                            ))}
                          </div>
                        </div>
                      </div>
                    </div>
                  )}

                  {/* STRUCTURE TAB */}
                  {activeTab === "structure" && (
                    <div>
                      <h3 className="text-lg font-bold text-white mb-6 flex items-center"><ChevronRight className="w-5 h-5 text-neon-blue mr-1" /> Page Framework</h3>
                      <div className="space-y-4">
                        {blueprint.structure.map((section, idx) => (
                          <div key={idx} className="bg-charcoal-800/40 p-5 rounded-xl border border-charcoal-700 relative overflow-hidden group">
                            <div className="absolute left-0 top-0 bottom-0 w-1 bg-charcoal-600 group-hover:bg-neon-blue transition-colors"></div>
                            <div className="flex justify-between items-start mb-2 pl-3">
                              <h4 className="text-md font-semibold text-white">{idx + 1}. {section.section_name}</h4>
                              <span className="text-xs font-mono text-slate-500 bg-charcoal-900 px-2 py-1 rounded">{section.container_settings}</span>
                            </div>
                            <div className="flex flex-wrap gap-2 pl-3 mt-4">
                              {section.elements_to_add.map((el, eIdx) => (
                                <span key={eIdx} className="text-xs bg-charcoal-700/50 text-slate-300 px-2.5 py-1 rounded-md border border-charcoal-600">
                                  {el}
                                </span>
                              ))}
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}

                  {/* COPY TAB */}
                  {activeTab === "copy" && (
                    <div className="space-y-6">
                      <h3 className="text-lg font-bold text-white mb-4 flex items-center"><ChevronRight className="w-5 h-5 text-neon-blue mr-1" /> Messaging Matrix</h3>

                      <div className="bg-charcoal-800/40 border border-charcoal-700 rounded-xl overflow-hidden group">
                        <div className="bg-charcoal-800/80 px-4 py-2 border-b border-charcoal-700 flex justify-between items-center">
                          <span className="text-xs uppercase text-slate-500 font-semibold tracking-wider">Hero Headline (H1)</span>
                          <button onClick={() => copyToClipboard(blueprint.copy.hero_h1, 'h1')} className="text-slate-500 hover:text-neon-blue transition-colors">
                            {copiedIndex === 'h1' ? <CheckCircle2 className="w-4 h-4 text-green-400" /> : <Copy className="w-4 h-4" />}
                          </button>
                        </div>
                        <div className="p-6">
                          <h1 className="text-3xl font-bold text-white">{blueprint.copy.hero_h1}</h1>
                        </div>
                      </div>

                      <div className="bg-charcoal-800/40 border border-charcoal-700 rounded-xl overflow-hidden group">
                        <div className="bg-charcoal-800/80 px-4 py-2 border-b border-charcoal-700 flex justify-between items-center">
                          <span className="text-xs uppercase text-slate-500 font-semibold tracking-wider">Subheadline</span>
                          <button onClick={() => copyToClipboard(blueprint.copy.hero_subheadline, 'sub')} className="text-slate-500 hover:text-neon-blue transition-colors">
                            {copiedIndex === 'sub' ? <CheckCircle2 className="w-4 h-4 text-green-400" /> : <Copy className="w-4 h-4" />}
                          </button>
                        </div>
                        <div className="p-6">
                          <p className="text-lg text-slate-300">{blueprint.copy.hero_subheadline}</p>
                        </div>
                      </div>

                      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div className="bg-charcoal-800/40 border border-charcoal-700 rounded-xl overflow-hidden group">
                          <div className="bg-charcoal-800/80 px-4 py-2 border-b border-charcoal-700 flex justify-between items-center">
                            <span className="text-xs uppercase text-slate-500 font-semibold tracking-wider">Primary Call To Action</span>
                            <button onClick={() => copyToClipboard(blueprint.copy.primary_cta, 'cta')} className="text-slate-500 hover:text-neon-blue transition-colors">
                              {copiedIndex === 'cta' ? <CheckCircle2 className="w-4 h-4 text-green-400" /> : <Copy className="w-4 h-4" />}
                            </button>
                          </div>
                          <div className="p-6 text-center">
                            <span className="inline-block bg-neon-blue text-charcoal-900 font-bold px-6 py-3 rounded-full shadow-[0_0_15px_rgba(0,240,255,0.3)]">
                              {blueprint.copy.primary_cta}
                            </span>
                          </div>
                        </div>

                        <div className="bg-charcoal-800/40 border border-charcoal-700 rounded-xl overflow-hidden">
                          <div className="bg-charcoal-800/80 px-4 py-2 border-b border-charcoal-700">
                            <span className="text-xs uppercase text-slate-500 font-semibold tracking-wider">Key Benefits</span>
                          </div>
                          <div className="p-5">
                            <ul className="space-y-3">
                              {blueprint.copy.feature_bullets.map((bullet, idx) => (
                                <li key={idx} className="flex items-start text-sm">
                                  <Sparkles className="w-4 h-4 text-neon-blue mr-3 shrink-0 mt-0.5" />
                                  <span className="text-slate-300">{bullet}</span>
                                </li>
                              ))}
                            </ul>
                          </div>
                        </div>
                      </div>
                    </div>
                  )}

                  {/* CODE TAB */}
                  {activeTab === "code" && (
                    <div>
                      <h3 className="text-lg font-bold text-white mb-6 flex items-center"><ChevronRight className="w-5 h-5 text-neon-blue mr-1" /> Structural Hacks & Integrations</h3>
                      <div className="space-y-6">
                        {blueprint.code.map((item, idx) => (
                          <div key={idx} className="bg-[#0d1117] rounded-xl border border-charcoal-700 overflow-hidden">
                            <div className="bg-charcoal-800 px-4 py-3 flex justify-between items-center border-b border-charcoal-700">
                              <div className="flex items-center space-x-2">
                                <FileCode2 className="w-4 h-4 text-neon-blue" />
                                <span className="font-semibold text-white text-sm">{item.plugin_name}</span>
                              </div>
                              <button
                                onClick={() => copyToClipboard(item.code_snippet, `code-${idx}`)}
                                className="flex items-center space-x-1 hover:bg-charcoal-700 px-2 py-1 rounded text-xs text-slate-400 hover:text-white transition-all"
                              >
                                {copiedIndex === `code-${idx}` ? (
                                  <><CheckCircle2 className="w-3 h-3 text-green-400" /><span>Copied</span></>
                                ) : (
                                  <><Copy className="w-3 h-3" /><span>Copy Code</span></>
                                )}
                              </button>
                            </div>
                            <div className="p-4 border-b border-charcoal-800">
                              <p className="text-sm text-slate-400">{item.instructions}</p>
                            </div>
                            <div className="p-4 overflow-x-auto">
                              <pre className="text-xs font-mono text-slate-300">
                                <code>{item.code_snippet}</code>
                              </pre>
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}
                </motion.div>
              </AnimatePresence>
            </div>
          </div>
        ) : null}
      </div>
    </div>
  );
}
