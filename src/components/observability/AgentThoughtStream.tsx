import React, { useState } from 'react';

interface AgentThoughtStreamProps {
  thoughtText: string;
  agentRole: string;
  latencyMs: number;
  isStreaming: boolean;
}

export const AgentThoughtStream: React.FC<AgentThoughtStreamProps> = ({
  thoughtText,
  agentRole,
  latencyMs,
  isStreaming,
}) => {
  const [isExpanded, setIsExpanded] = useState(true);

  if (!thoughtText) return null;

  return (
    <div className="bg-slate-900/90 border border-indigo-500/30 rounded-xl p-4 my-3 backdrop-blur shadow-lg transition-all">
      <div 
        className="flex items-center justify-between cursor-pointer select-none"
        onClick={() => setIsExpanded(!isExpanded)}
      >
        <div className="flex items-center gap-2">
          <span className="relative flex h-3 w-3">
            {isStreaming && (
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-indigo-400 opacity-75"></span>
            )}
            <span className="relative inline-flex rounded-full h-3 w-3 bg-indigo-500"></span>
          </span>
          <span className="text-xs font-semibold uppercase tracking-wider text-indigo-300">
            {agentRole} Extended Reasoning
          </span>
        </div>
        <div className="flex items-center gap-3">
          <span className="text-xs font-mono text-slate-400">
            {latencyMs > 0 ? `${latencyMs}ms` : 'thinking...'}
          </span>
          <span className="text-xs text-slate-400">
            {isExpanded ? '▲' : '▼'}
          </span>
        </div>
      </div>

      {isExpanded && (
        <div className="mt-3 text-sm text-slate-300 font-mono bg-slate-950/60 p-3 rounded-lg border border-slate-800 whitespace-pre-wrap leading-relaxed">
          {thoughtText}
        </div>
      )}
    </div>
  );
};
