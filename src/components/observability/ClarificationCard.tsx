import React, { useState } from 'react';

interface ClarificationOption {
  id: string;
  label: string;
  description: string;
  target_tag: string;
}

interface ClarificationCardProps {
  question: string;
  options: ClarificationOption[];
  depth: number;
  maxDepth: number;
  breadcrumbs: string[];
  onSelect: (optionId: string, tag: string) => void;
  onWriteInSubmit: (customText: string) => void;
}

export const ClarificationCard: React.FC<ClarificationCardProps> = ({
  question,
  options,
  depth,
  maxDepth,
  breadcrumbs,
  onSelect,
  onWriteInSubmit,
}) => {
  const [customText, setCustomText] = useState('');

  return (
    <div className="bg-gradient-to-br from-slate-900 via-indigo-950/40 to-slate-900 border-2 border-indigo-500/60 rounded-2xl p-5 my-4 shadow-2xl backdrop-blur">
      {/* Breadcrumb Context Trail */}
      <div className="flex items-center gap-2 mb-3 text-xs font-mono text-slate-400">
        <span>Context Trail:</span>
        {breadcrumbs.map((crumb, idx) => (
          <React.Fragment key={idx}>
            <span className="px-2 py-0.5 bg-slate-800 text-indigo-300 rounded font-semibold border border-slate-700">
              {crumb}
            </span>
            {idx < breadcrumbs.length - 1 && <span className="text-slate-600">▶</span>}
          </React.Fragment>
        ))}
        <span className="ml-auto text-[10px] text-amber-300 bg-amber-950/60 border border-amber-800/80 px-2 py-0.5 rounded">
          Clarification Step {depth} of {maxDepth}
        </span>
      </div>

      <h4 className="text-sm font-semibold text-white mb-3">
        ❓ {question}
      </h4>

      {/* Quick Selection Option Pills */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-4">
        {options.map((opt) => (
          <button
            key={opt.id}
            onClick={() => onSelect(opt.id, opt.target_tag)}
            className="flex flex-col items-start p-3 rounded-xl bg-slate-950/80 border border-slate-800 hover:border-indigo-500 hover:bg-indigo-900/30 transition-all text-left group"
          >
            <span className="text-xs font-bold font-mono text-indigo-300 group-hover:text-white">
              {opt.label}
            </span>
            <span className="text-[11px] text-slate-400 mt-1 line-clamp-1">
              {opt.description}
            </span>
          </button>
        ))}
      </div>

      {/* Write-in Fallback */}
      <div className="flex items-center gap-2 pt-3 border-t border-slate-800/80">
        <input
          type="text"
          placeholder="Or specify another equipment tag..."
          value={customText}
          onChange={(e) => setCustomText(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === 'Enter' && customText.trim()) {
              onWriteInSubmit(customText.trim());
            }
          }}
          className="flex-1 bg-slate-950 border border-slate-800 rounded-lg px-3 py-1.5 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500"
        />
        <button
          onClick={() => customText.trim() && onWriteInSubmit(customText.trim())}
          className="px-4 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded-lg text-xs font-semibold transition-all"
        >
          Submit
        </button>
      </div>
    </div>
  );
};
