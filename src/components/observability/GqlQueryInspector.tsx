import React, { useState } from 'react';

interface GqlQueryInspectorProps {
  rawGql: string;
  executionTimeMs: number;
  rowsReturned: number;
  trueTimeToken?: string;
}

export const GqlQueryInspector: React.FC<GqlQueryInspectorProps> = ({
  rawGql,
  executionTimeMs,
  rowsReturned,
  trueTimeToken = "0x4e29b109_truetime",
}) => {
  const [activeTab, setActiveTab] = useState<'gql' | 'path'>('gql');

  return (
    <div className="bg-slate-900/90 border border-emerald-500/40 rounded-xl p-4 my-3 shadow-lg">
      <div className="flex items-center justify-between border-b border-slate-800 pb-2 mb-3">
        <div className="flex items-center gap-2">
          <span className="text-xs font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 font-mono">
            CLOUD SPANNER ISO GQL
          </span>
          <span className="text-xs font-mono text-slate-400">
            {rowsReturned} rows in {executionTimeMs}ms
          </span>
        </div>
        <div className="flex items-center gap-2">
          <span className="text-[10px] font-mono bg-slate-800 text-slate-400 px-2 py-0.5 rounded">
            TrueTime: {trueTimeToken}
          </span>
          <div className="flex rounded-lg border border-slate-700 overflow-hidden text-xs">
            <button
              onClick={() => setActiveTab('gql')}
              className={`px-2.5 py-1 ${activeTab === 'gql' ? 'bg-indigo-600 text-white font-semibold' : 'bg-slate-800 text-slate-400'}`}
            >
              Query
            </button>
            <button
              onClick={() => setActiveTab('path')}
              className={`px-2.5 py-1 ${activeTab === 'path' ? 'bg-indigo-600 text-white font-semibold' : 'bg-slate-800 text-slate-400'}`}
            >
              Graph Path
            </button>
          </div>
        </div>
      </div>

      {activeTab === 'gql' ? (
        <pre className="text-xs font-mono bg-slate-950 p-3 rounded-lg border border-slate-800 text-emerald-300 overflow-x-auto whitespace-pre-wrap">
          {rawGql}
        </pre>
      ) : (
        <div className="bg-slate-950 p-4 rounded-lg border border-slate-800 flex items-center justify-center gap-4 text-xs font-mono">
          <div className="px-3 py-2 bg-indigo-900/60 border border-indigo-500 rounded-lg text-indigo-200">
            🔵 Instruments (TXSHH-0502A)
          </div>
          <span className="text-slate-500 font-bold">───[:ACTUATES_INTERLOCK]───▶</span>
          <div className="px-3 py-2 bg-purple-900/60 border border-purple-500 rounded-lg text-purple-200">
            🟢 Equipment (E-2303)
          </div>
        </div>
      )}
    </div>
  );
};
