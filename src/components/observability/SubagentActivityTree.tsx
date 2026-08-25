import React from 'react';

interface SubagentActivityProps {
  subagentName: string;
  taskDescription: string;
  status: 'DISPATCHED' | 'EXECUTING' | 'COMPLETED' | 'ERROR';
}

export const SubagentActivityTree: React.FC<SubagentActivityProps> = ({
  subagentName,
  taskDescription,
  status,
}) => {
  const getBadgeStyle = () => {
    switch (status) {
      case 'DISPATCHED':
      case 'EXECUTING':
        return 'bg-amber-500/20 text-amber-300 border-amber-500/40 animate-pulse';
      case 'COMPLETED':
        return 'bg-emerald-500/20 text-emerald-300 border-emerald-500/40';
      case 'ERROR':
        return 'bg-rose-500/20 text-rose-300 border-rose-500/40';
      default:
        return 'bg-slate-800 text-slate-400 border-slate-700';
    }
  };

  return (
    <div className="flex items-start gap-3 my-2 pl-4 border-l-2 border-indigo-500/30">
      <div className="flex-1 bg-slate-900/60 border border-slate-800 rounded-lg p-3">
        <div className="flex items-center justify-between">
          <span className="font-semibold text-xs text-indigo-200">
            🤖 Delegated to: <code className="text-indigo-400 font-mono">{subagentName}</code>
          </span>
          <span className={`text-[10px] px-2 py-0.5 rounded-full border font-mono ${getBadgeStyle()}`}>
            {status}
          </span>
        </div>
        <p className="text-xs text-slate-400 mt-1">
          {taskDescription}
        </p>
      </div>
    </div>
  );
};
