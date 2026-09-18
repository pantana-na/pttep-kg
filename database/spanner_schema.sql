-- =============================================================================
-- Cloud Spanner Graph & Relational DDL for Phenol Process Safety Platform
-- Spec: SPEC-20260824-MULTI-AGENT-CLOUD-ARCHITECTURE Section 3.2.1
-- =============================================================================

-- 1. Unit & Equipment Relational Tables
CREATE TABLE IF NOT EXISTS Units (
  UnitId STRING(32) NOT NULL,
  Name STRING(128) NOT NULL,
  Code STRING(16) NOT NULL,
  Description STRING(MAX),
  Sources ARRAY<STRING(128)>,
  UpdatedAt TIMESTAMP OPTIONS (allow_commit_timestamp = true),
) PRIMARY KEY (UnitId);

CREATE TABLE IF NOT EXISTS Equipment (
  EquipmentTag STRING(64) NOT NULL,
  UnitId STRING(32) NOT NULL,
  Name STRING(128) NOT NULL,
  Type STRING(128) NOT NULL,
  DesignPressureBarg FLOAT64,
  DesignTempCelsius FLOAT64,
  OperatingPressureBarg FLOAT64,
  OperatingTempCelsius FLOAT64,
  Material STRING(64),
  MarkdownUri STRING(256),
  DescriptionSummary STRING(MAX),
  Embedding ARRAY<FLOAT64>(vector_length=>768),
  EquipmentTokens TOKENLIST AS (
    TOKENIZE_FULLTEXT(EquipmentTag || ' ' || Name || ' ' || IFNULL(DescriptionSummary, ''))
  ) HIDDEN,
  IsDeleted BOOL NOT NULL DEFAULT (false),
  UpdatedAt TIMESTAMP OPTIONS (allow_commit_timestamp = true),
) PRIMARY KEY (EquipmentTag);

CREATE TABLE IF NOT EXISTS Streams (
  StreamId STRING(64) NOT NULL,
  UnitId STRING(32) NOT NULL,
  Description STRING(128),
  FromEquipment STRING(64),
  ToEquipment STRING(64),
  FlowRateKgHr FLOAT64,
  TempCelsius FLOAT64,
  PressureBarg FLOAT64,
  ChpConcentrationWtPct FLOAT64,
  Phase STRING(32),
  IsDeleted BOOL NOT NULL DEFAULT (false),
) PRIMARY KEY (StreamId);

CREATE TABLE IF NOT EXISTS Instruments (
  InstrumentTag STRING(64) NOT NULL,
  EquipmentTag STRING(64) NOT NULL,
  Type STRING(128) NOT NULL,
  CalibratedRange STRING(64),
  TripSetpoint STRING(64),
  SilRating STRING(16),
  VotingLogic STRING(16),
  IsSisInitiator BOOL NOT NULL DEFAULT (false),
  InstrumentTokens TOKENLIST AS (
    TOKENIZE_FULLTEXT(InstrumentTag || ' ' || EquipmentTag || ' ' || Type || ' ' || IFNULL(TripSetpoint, ''))
  ) HIDDEN,
  IsDeleted BOOL NOT NULL DEFAULT (false),
) PRIMARY KEY (InstrumentTag);

CREATE TABLE IF NOT EXISTS ChemicalHazards (
  HazardId STRING(64) NOT NULL,
  ChemicalName STRING(128) NOT NULL,
  CasNumber STRING(32),
  DecompositionOnsetTempCelsius FLOAT64,
  SadtTempCelsius STRING(32),
  FlashPointCelsius FLOAT64,
  GhsClassification ARRAY<STRING(64)>,
  MarkdownUri STRING(256),
) PRIMARY KEY (HazardId);

-- 2. HAZOP Study Relational Entities
CREATE TABLE IF NOT EXISTS HazopNodes (
  NodeId STRING(32) NOT NULL,
  Name STRING(128) NOT NULL,
  UnitId STRING(32) NOT NULL,
  PidSheet STRING(128),
  Status STRING(32),
  IsDeleted BOOL NOT NULL DEFAULT (false),
) PRIMARY KEY (NodeId);

CREATE TABLE IF NOT EXISTS Deviations (
  DeviationId STRING(64) NOT NULL,
  NodeId STRING(32) NOT NULL,
  Parameter STRING(32) NOT NULL,
  Guideword STRING(32) NOT NULL,
  DeviationLabel STRING(64) NOT NULL,
  SequenceNumber INT64 NOT NULL,
  Embedding ARRAY<FLOAT64>(vector_length=>768),
) PRIMARY KEY (DeviationId);

CREATE TABLE IF NOT EXISTS Causes (
  CauseId STRING(64) NOT NULL,
  DeviationId STRING(64) NOT NULL,
  EquipmentTag STRING(64),
  Description STRING(MAX) NOT NULL,
) PRIMARY KEY (CauseId);

CREATE TABLE IF NOT EXISTS Consequences (
  ConsequenceId STRING(64) NOT NULL,
  CauseId STRING(64) NOT NULL,
  CausalChain STRING(MAX) NOT NULL,
  SeverityPeople INT64 NOT NULL,
  SeverityEnvironment INT64 NOT NULL,
  SeverityEconomic INT64 NOT NULL,
  SeveritySocial INT64 NOT NULL,
  InitialLikelihood INT64 NOT NULL,
  InitialRiskRating STRING(16) NOT NULL,
) PRIMARY KEY (ConsequenceId);

CREATE TABLE IF NOT EXISTS Safeguards (
  SafeguardId STRING(64) NOT NULL,
  ConsequenceId STRING(64) NOT NULL,
  InstrumentTag STRING(64),
  Description STRING(MAX) NOT NULL,
  IsInterlockEsd BOOL NOT NULL,
  IplCreditLevel INT64 NOT NULL,
) PRIMARY KEY (SafeguardId);

CREATE TABLE IF NOT EXISTS ActionItems (
  ActionId STRING(32) NOT NULL,
  ConsequenceId STRING(64) NOT NULL,
  NodeId STRING(32) NOT NULL,
  RecommendationText STRING(MAX) NOT NULL,
  RiskRank STRING(16) NOT NULL,
  Discipline STRING(64),
  OwnerType STRING(16),
  Owner STRING(128),
  DueDate DATE,
  Status STRING(16),
  MitigatedLikelihood INT64,
  MitigatedRiskRating STRING(16),
  ResidualLikelihood INT64,
  ResidualRiskRating STRING(16),
) PRIMARY KEY (ActionId);

-- 3. Graph Edge Tables
CREATE TABLE IF NOT EXISTS EquipmentFlows (
  FromEquipmentTag STRING(64) NOT NULL,
  ToEquipmentTag STRING(64) NOT NULL,
  StreamId STRING(64) NOT NULL,
  PRIMARY KEY (FromEquipmentTag, ToEquipmentTag, StreamId),
  FOREIGN KEY (FromEquipmentTag) REFERENCES Equipment(EquipmentTag),
  FOREIGN KEY (ToEquipmentTag) REFERENCES Equipment(EquipmentTag),
  FOREIGN KEY (StreamId) REFERENCES Streams(StreamId)
);

CREATE TABLE IF NOT EXISTS NodeEquipmentMap (
  NodeId STRING(32) NOT NULL,
  EquipmentTag STRING(64) NOT NULL,
  PRIMARY KEY (NodeId, EquipmentTag),
  FOREIGN KEY (NodeId) REFERENCES HazopNodes(NodeId),
  FOREIGN KEY (EquipmentTag) REFERENCES Equipment(EquipmentTag)
);

CREATE TABLE IF NOT EXISTS InstrumentActuations (
  InitiatorInstrumentTag STRING(64) NOT NULL,
  TargetEquipmentTag STRING(64) NOT NULL,
  InterlockAction STRING(64) NOT NULL,
  PRIMARY KEY (InitiatorInstrumentTag, TargetEquipmentTag),
  FOREIGN KEY (InitiatorInstrumentTag) REFERENCES Instruments(InstrumentTag),
  FOREIGN KEY (TargetEquipmentTag) REFERENCES Equipment(EquipmentTag)
);

-- 4. Full-Text Search Indexes
CREATE SEARCH INDEX EquipmentKeywordSearchIndex ON Equipment(EquipmentTokens);

CREATE SEARCH INDEX InstrumentsKeywordSearchIndex ON Instruments(InstrumentTokens);

-- 5. Property Graph Definition (ISO GQL Standard)
CREATE OR REPLACE PROPERTY GRAPH PhenolProcessSafetyGraph
  NODE TABLES (
    Units,
    Equipment,
    Streams,
    Instruments,
    ChemicalHazards,
    HazopNodes,
    Deviations,
    Causes,
    Consequences,
    Safeguards,
    ActionItems
  )
  EDGE TABLES (
    EquipmentFlows
      SOURCE KEY (FromEquipmentTag) REFERENCES Equipment(EquipmentTag)
      DESTINATION KEY (ToEquipmentTag) REFERENCES Equipment(EquipmentTag)
      LABEL FEEDS,
    NodeEquipmentMap
      SOURCE KEY (NodeId) REFERENCES HazopNodes(NodeId)
      DESTINATION KEY (EquipmentTag) REFERENCES Equipment(EquipmentTag)
      LABEL ENCOMPASSES,
    InstrumentActuations
      SOURCE KEY (InitiatorInstrumentTag) REFERENCES Instruments(InstrumentTag)
      DESTINATION KEY (TargetEquipmentTag) REFERENCES Equipment(EquipmentTag)
      LABEL ACTUATES_INTERLOCK
  );
