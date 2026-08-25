import React, { useState } from 'react';

interface ToolExecutionCardProps {
  toolName: string;
  args: Record<string, any>;
  resultPreview?: string;
  latencyMs?: number;
  isExecuting: boolean;
}

export const ToolExecutionCard: React.FC<ToolExecutionCardProps> = ({
  toolName,
  args,
  resultPreview,
  latencyMs,
  isExecuting,
}) => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="bg-slate-900 border border-slate-700/60 rounded-xl p-3 my-2 shadow-md">
      <div 
        className="flex items-center justify-between cursor-pointer select-none"
        onClick={() => setIsOpen(!isOpen)}
      >
        <div className="flex items-center gap-2">
          <span className="text-xs px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 font-mono font-bold">
            TOOL
          </span>
          <code className="text-xs font-mono text-cyan-200 font-semibold">{toolName}</code>
        </div>
        <div className="flex items-center gap-3">
          {latencyMs !== undefined && (
            <span className="text-[11px] font-mono text-emerald-400">
              ⚡ {latencyMs}ms
            </span>
          )}
          {isExecuting && (
            <span className="text-xs text-amber-400 animate-pulse font-mono">
              executing...
            </span>
          )}
          <span className="text-xs text-slate-400">
            {isOpen ? '▲' : '▼'}
          </span>
        </div>
      </div>

      {isOpen && (
        <div className="mt-3 space-y-2 text-xs font-mono">
          <div className="bg-slate-950 p-2.5 rounded border border-slate-800">
            <span className="text-slate-500 uppercase tracking-wider text-[10px] block mb-1">Arguments:</span>
            <pre className="text-slate-300 overflow-x-auto">{JSON.stringify(args, null, 2)}</pre>
          </div>
          {resultPreview && (
            <div className="bg-slate-950 p-2.5 rounded border border-slate-800">
              <span className="text-slate-500 uppercase tracking-wider text-[10px] block mb-1">Result Preview:</span>
              <p className="text-slate-300">{resultPreview}</p>
            </div>
          )}
        </div>
      )}
    </div>
  );
};
