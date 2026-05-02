In Google Antigravity, Customization goes far beyond UI themes; it forms the governance layer that dictates how your AI agents operate, what they know, and what they can access.

To tailor my explanations, how familiar are you with Antigravity or other AI coding assistants?

Based on your experience, we can follow this straightforward plan to cover the system:

1. **Rules:** Persistent guidelines and constraints.
2. **Workflows:** Reusable, step-by-step procedures.
3. **Skills:** On-demand knowledge and tool modules.
4. **MCP Integrations:** Connections to external databases and APIs.
5. **Agent Settings:** Trust boundaries and security modes.

In Google Antigravity, customization and extensibility replace traditional coding plugins with a "governance layer" that directs your AI agents. Because the system is "agent-first," you extend it by teaching the AI new behaviors using simple Markdown and YAML files rather than writing complex extension code.

Following our plan, the foundation of this system starts with **Rules**.

Rules are Markdown files where you define persistent constraints, like your preferred coding style or specific security boundaries. You can set them globally or for a specific workspace, and they can be triggered automatically, manually, or based on the file types you are working on.

The main difference is that **Rules** are passive guidelines, while **Workflows** are active, step-by-step procedures.

Rules sit in the background to provide persistent context, telling the agent _how_ to behave generally, such as enforcing a specific coding style or security mandate.

Workflows, on the other hand, guide the agent through a specific series of repetitive tasks, like deploying a service or responding to pull request comments. You trigger them manually using a slash command like `/workflow-name`. You can even ask the agent to automatically generate a Workflow for you based on a recent conversation history.

Skills are modular packages of knowledge that teach the AI how to approach specific types of tasks, such as following your team's testing conventions or code review processes.

Unlike Workflows that you must trigger manually, Skills use a "progressive disclosure" pattern. You don't have to explicitly tell the agent to use a skill; it dynamically discovers and activates the skill in the background whenever your current task matches the skill's description.

To build a skill, you create a dedicated folder (either globally or in your workspace's `.agents/skills/` directory) containing a `SKILL.md` file. This file requires a YAML header with a name and a highly specific description—this description is critical because it acts as the trigger for the agent.

You can also bundle extra scripts or reference documents within the skill folder. Just keep in mind a crucial system rule: if you link to these extra resources within your `SKILL.md`, you must use absolute `file:///` paths rather than relative paths to ensure the agent doesn't lose track of the files.



Rules are straightforward Markdown files (up to 12,000 characters) that act as persistent instructions for your agents. In the context of extensibility, they replace traditional coded plugins; you simply write plain text to define coding styles, security boundaries, or stack preferences without needing to learn a complex extension API.

You can organize these Rules in two ways:

* **Global:** Stored in `~/.gemini/GEMINI.md` (or `AGENTS.md`) to apply across all your workspaces.
* **Workspace:** Stored in your project's `.agents/rules/` folder for project-specific constraints.

You also have granular control over when they activate. They can be "Always On", triggered manually with an `@mention`, set to activate for specific file types using glob patterns (like `*.js`), or left to the model's discretion. You can even build a web of constraints by referencing other Markdown files directly inside your rules using `@filename` syntax.

Glob mode automatically applies a Rule only when you are working on specific files that match a pattern, like `*.js` or `src/**/*.ts`. For instance, you could create a rule enforcing specific formatting guidelines that only activates when you open a CSS file.

In addition to Glob, you can set Rules to be "Always On" for constant enforcement, "Manual" to trigger them yourself with an `@mention`, or "Model Decision" to let the AI automatically apply them based on the context of your task.

You can use the `@filename` syntax inside your Rule files to directly reference and link other documents.

How the system finds the file depends on how you write the path:

* **Relative paths:** Interpreted based on the location of the Rule file itself.
* **Absolute paths:** The system tries to find the exact system path first. If that file doesn't exist, it falls back to resolving it relative to your workspace repository.

This makes it easy to chain different constraints together without writing one massive text file.

Interestingly, Antigravity does not actually have a built-in way to resolve conflicting rules automatically. If two rules contradict each other, the AI model has to guess, which leads to unpredictable results.

To solve this, you need to explicitly define your own "Precedence Matrix" inside your global `AGENTS.md` file. For example, you can write a rule that explicitly states security mandates always override core coding rules, which in turn override skill-level rules.

To create a Precedence Matrix, you simply add a dedicated subsection inside your `AGENTS.md` file that explicitly ranks the priority of your rules.

You can do this by adding a header like `### Conflict Resolution Precedence` and clearly defining the hierarchy. For example, you might write: `security-mandate.md → gsd-core-rules.md → skill-level rules`. It is also a best practice to define a fallback, such as stating that any conflict between rules on the exact same tier automatically escalates to `STRICT_MODE` before the agent can proceed.

Both Rule and Workflow files have a strict limit of 12,000 characters each.

Workspace Rules are project-specific constraints stored as Markdown files inside the `.agents/rules/` directory at the root of your project.

While Global Rules (like `~/.gemini/GEMINI.md`) apply to every environment you use, Workspace Rules allow you to tailor behaviors—such as specific coding styles or testing requirements—strictly for the current repository. You can store multiple rule files in this folder, and they can be created manually in your editor or by clicking the "+ Workspace" button in the Customizations UI. Antigravity also maintains backward compatibility with the older `.agent/rules/` directory format.



The Mechanics of Progressive Disclosure in Agent Skills

The progressive disclosure pattern is the three-step mechanism Google Antigravity uses to efficiently manage how and when the agent loads Agent Skills into its active context [1]. Instead of overwhelming the agent by loading the full text of every available skill at the start of a conversation, this pattern ensures that the agent's context window remains focused on the immediate task by only revealing instructions when they are actually needed [1, 2].

The progressive disclosure pattern operates in the following three phases:

**1. Discovery**At the beginning of a conversation, the agent does not read the complete contents of your skill files [1]. Instead, it performs a lightweight scan where it only reviews a list of available skills, specifically looking at the `name` and `description` fields located in the YAML frontmatter of your `SKILL.md` files [1, 3].

**2. Activation**As you assign tasks, the agent evaluates your prompt against the descriptions it read during the Discovery phase [1]. If the agent determines that a particular skill is relevant to the problem at hand, it will automatically "activate" the skill by pulling the full instructions into its context [1]. While the agent typically makes this decision autonomously based on the context of the task, you can also bypass this process and ensure a skill is activated by explicitly mentioning the skill by name in your prompt [1].

**3. Execution**Once a skill is activated, the agent reads the complete contents of the `SKILL.md` file [1]. During this phase, it applies the specific instructions, best practices, and decision trees defined in the skill, and may utilize any optional scripts or resources bundled within the skill's folder to complete the work [1, 4, 5].

To ensure the progressive disclosure pattern functions optimally, the sources highlight several architectural best practices for creating skills:

* **Write Highly Specific Descriptions:** Because the agent relies entirely on the `description` field during the Discovery phase to decide whether to activate a skill, this field must clearly articulate exactly what the skill does and when it should be used [2, 3]. It is recommended to write descriptions in the third person using targeted keywords, such as "Generates unit tests for Python code using pytest conventions" [1].
* **Maintain a Focused Scope:** A skill should be designed to do exactly one thing well [2]. Creating monolithic, "do everything" skills undermines the progressive disclosure pattern, as activating the skill would force the agent to load massive amounts of irrelevant instructions into its context [2]. Separate distinct tasks into their own individual skills [2].
* **Treat Scripts as Black Boxes:** During the Execution phase, if your skill includes auxiliary scripts, your `SKILL.md` instructions should encourage the agent to execute them with a `--help` flag rather than reading the actual source code of the script [2]. This prevents the agent from analyzing large files unnecessarily, keeping its context tightly focused on the task [2].

--------------------------------------------------------------------------------

Architecting Workflow-to-Skill Invocations

Antigravity Mission Control online. Full platform context loaded. Planning-first sequence initiated…

Mission Brief

Yes, a Workflow can ensure a Skill is called by explicitly mentioning the skill by name within its sequential steps [1]. While Workflows natively support executing other Workflows directly via slash commands [2], Skills operate on a progressive disclosure model where the agent usually activates them based on context [1]. However, explicitly writing the skill's name into a workflow step forces the agent's contextual routing to activate it [1].

Detailed Plan
    task_group:
      goal: "Deconstruct the invocation bridging between Workflows (sequential steps) and Skills (progressive capabilities)."
      execution_phases:
        - phase_1_orchestration:
            sub_agent: "Planner Agent"
            action: "Analyze explicit workflow-to-workflow nesting vs. workflow-to-skill activation."
        - phase_2_context_mapping:
            sub_agent: "Research Agent"
            action: "Cross-reference Workflow prompt sequencing with manual Skill mention capabilities."
        - phase_3_risk_evaluation:
            sub_agent: "Critique &amp; Risk Agent"
            action: "Evaluate context window bloating when a single workflow activates multiple heavy skills simultaneously."
        - phase_4_synthesis:
            sub_agent: "Coder/Builder Agent"
            action: "Generate a production-grade Workflow artifact demonstrating forced Skill activation."



Agent Execution Summary

* **Planner Agent track:** Mapped the native invocation patterns. Workflows can explicitly call other Workflows using instructions like “Call `/workflow-2`” [2].
* **Research Agent track:** Confirmed the Skill activation bridge. Skills are generally discovered and activated autonomously based on task context, but the documentation explicitly notes that "you can mention a skill by name if you want to ensure it's used" [1].
* **Critique Agent flag:** _Context Protection Alert._ Because Workflows sequentially process a series of steps and prompts [2, 3], forcefully mentioning multiple complex skills within a single Workflow file will bypass the agent's natural progressive disclosure optimizations [1], pulling the Markdown of every mentioned skill into the context window simultaneously and risking token quota exhaustion.

Deep Insights & Opportunities

Layer 1: The Contextual Bridge

Workflows and Skills operate on different routing mechanisms. Workflows provide a "structured sequence of steps or prompts" [3]. Because a workflow step acts as a prompt, it inherently provides the context the agent uses to evaluate the `description` fields of your available Skills [1, 4]. Therefore, simply describing a task in a Workflow step that aligns heavily with a Skill's YAML description will often naturally trigger the Skill during execution via progressive disclosure [1].

Layer 2: Forced Manual Activation

If you cannot rely on the agent's contextual deduction, you can hardcode the connection. The platform rules dictate that while you don't _need_ to explicitly tell the agent to use a skill, you are allowed to "mention a skill by name" to guarantee its activation [1]. By embedding this explicit mention directly into the markdown steps of your Workflow, you create a direct pipeline from a slash-invoked trajectory to a specialized capability [3, 5].

Risks & Mitigations

1. **Risk: Bypassing Progressive Disclosure**
2. _Issue:_ The progressive disclosure pattern protects the reasoning window by only loading the full `SKILL.md` instructions when necessary [1]. Explicitly calling multiple heavy skills in a single workflow forces the agent to load all of those constraints at once.
3. _Mitigation:_ Keep workflows modular. Use Workflows to call other Workflows (e.g. "Call `/workflow-2`") [2], and only explicitly mention a Skill by name when that specific execution step absolutely requires the bundled knowledge package or auxiliary scripts [1, 5].

Deliverables

**Enterprise Workflow-to-Skill Integration (****.agents/workflows/secure-deploy.md****)** _Deploy this Workflow to see how trajectory sequencing can explicitly trigger a Reusable Knowledge Package._
    # Secure Deployment Pipeline
    **Description:** Sequentially prepares the workspace and triggers the custom deployment skill.

    ## Step 1: Pre-Deployment Audit
    - Review the workspace for any uncommitted changes.
    - Ensure all tests pass before proceeding.

    ## Step 2: Triggering the Skill
    - I want you to explicitly use the skill named `firebase-secure-deploy`.
    - Follow its embedded best practices and scripts exactly to execute the deployment.



Recommended Next Actions

1. **Map Your Capabilities:** Review your `.agents/skills/` directory to identify the exact `name` fields registered in your YAML frontmatter [4, 6].
2. **Embed Mentions:** Open an existing Workflow in your Customizations panel [2] and add a step that explicitly mentions one of those exact skill names [1].
3. **Test the Chain:** Run the Workflow using `/workflow-name` in the chat [2] and monitor the Agent Manager to ensure the skill is successfully brought into context and executed.

Verification Checklist

* [x] Addressed the capability of calling Skills from Workflows.
* [x] Cited the manual mention mechanic for ensuring Skill usage [1].
* [x] Contrasted this with native Workflow-to-Workflow invocation [2].
* [x] Detailed the token-exhaustion risks of bypassing progressive disclosure [1].

--------------------------------------------------------------------------------

Mechanics of Google Antigravity Skill Activation

In Google Antigravity, the agent decides to activate a skill using a "progressive disclosure" pattern that relies heavily on context and the skill's description [1, 2].

Here is how the decision process works:

* **Discovery Phase:** When you start a conversation, the agent does not load the entirety of every skill. Instead, it performs a lightweight scan where it only sees the `name` and `description` fields located in the YAML frontmatter of the available skills [1].
* **Contextual Evaluation:** The agent reads the `description` field to understand what the skill does and when it should be used [3]. It then evaluates this description against the context of your current task to determine if the skill is relevant [1].
* **Activation:** If the agent decides the skill is applicable to your prompt, it automatically activates the skill by pulling the full Markdown instructions from the `SKILL.md` file into its active context so it can execute the task [1].

While the agent typically decides to use a skill on its own based on this context, you can also manually force the agent to activate a specific skill by mentioning it by name in your prompt [1].

--------------------------------------------------------------------------------

The Antigravity Triad: Rules, Workflows, and Skills

In Google Antigravity, Rules, Workflows, and Skills form the core extensibility triad, but they serve distinct purposes regarding how they shape and trigger agent behavior:

**Rules (Persistent Constraints)**Rules are manually defined constraints that dictate the agent's style, tech stack preferences, and safety boundaries [1-3]. They provide "persistent, reusable context at the prompt level" [4]. Structured entirely as Markdown files, they are stored globally (e.g., `~/.gemini/GEMINI.md`) or per-workspace (e.g., `.agents/rules/`) [1, 3, 5]. Rules act as passive guidelines that are injected into the agent's prompt based on specific activation modes, such as "Always On," file Glob patterns (e.g., `*.js`), Model Decisions, or manual `@mentions` [5].

**Workflows (Sequential Trajectories)**While Rules dictate _how_ the agent should behave, Workflows dictate _what steps_ the agent should take. Workflows provide a "structured sequence of steps or prompts at the trajectory level," guiding the model through interconnected tasks like deploying a service or responding to PR comments [4]. Also saved as Markdown files, Workflows are actively invoked by the user via slash commands (e.g., `/workflow-name`) [4, 6]. Workflows can be composable and nested, allowing one workflow file to sequentially call other workflows [6].

**Skills (Progressive Capabilities)**Skills act as the agent's dynamic toolbelt. They are defined as "reusable packages of knowledge that extend what the agent can do" [7]. Unlike Rules and Workflows, a Skill is not just a single Markdown file; it is structured as a dedicated folder containing a `SKILL.md` file with YAML frontmatter, alongside optional auxiliary scripts and resources [7-9]. Furthermore, Skills operate on a "progressive disclosure" pattern rather than being permanently injected or slash-invoked [10]. During the "Discovery" phase, the agent reads only the YAML `description` field [9, 10]. If the agent determines the skill is relevant to your current task, it automatically "Activates" the skill, reading the full Markdown instructions and executing any bundled scripts to complete the work [10].

--------------------------------------------------------------------------------

Modular Architecture and Rule Nesting in Google Antigravity

Antigravity Mission Control online. Full platform context loaded. Planning-first sequence initiated…

Mission Brief

Yes, Google Antigravity fully supports using `@filename` mentions to nest multiple Rules files [1]. By allowing multiple Markdown files within the `.agents/rules/` directory and enabling dynamic cross-referencing, the platform allows you to bypass the strict 12,000-character per-file limit and construct modular, composable governance trees [1-3].

Detailed Plan
    task_group:
      goal: "Deconstruct the @filename mention syntax for nesting and modularizing Rule files in Antigravity."
      execution_phases:
        - phase_1_orchestration:
            sub_agent: "Planner Agent"
            action: "Map the syntactic rules for @mentions within Markdown rule files."
        - phase_2_context_mapping:
            sub_agent: "Research/Deep-Dive Agent"
            action: "Analyze path resolution logic (relative vs. absolute fallbacks)."
        - phase_3_risk_evaluation:
            sub_agent: "Critique &amp; Risk Agent"
            action: "Evaluate pathing breakage risks and token bloat from excessive nesting."
        - phase_4_synthesis:
            sub_agent: "Coder/Builder Agent"
            action: "Generate a production-grade composable rule architecture demonstrating nested includes."



Agent Execution Summary

* **Planner Agent track:** Verified capability. Antigravity explicitly allows multiple Markdown files within the `.agents/rules/` folder [2]. Within these files, you can reference other files using the `@filename` syntax [1].
* **Research Agent track:** Mapped the pathing resolution cascade. The platform distinguishes between relative paths (resolving relative to the Rules file itself) and absolute paths (attempting OS-level resolution first, then falling back to the repository workspace root) [1].
* **Critique Agent flag:** _Context Exhaustion Risk._ While individual rule files are hard-capped at 12,000 characters [3], utilizing `@mentions` pulls the text of the nested files into the reasoning model's context window. Deeply nested rule trees triggered via "Always On" activation will rapidly burn through the 5-hour rolling Vertex AI token quota due to massive prompt inflation [3, 4].

Deep Insights & Opportunities

Layer 1: The `@filename` Syntax & Modularity

In Antigravity, you are not forced to maintain a monolithic `GEMINI.md` file. You can break your constraints into modular files (e.g., `frontend-rules.md`, `security-rules.md`) [3, 5]. Inside any rule file, you can type `@filename` to pull the contents of another file directly into the agent's context [1]. This effectively acts as an "import" statement for your agent's behavioral instructions, allowing you to nest logic.

Layer 2: Advanced Path Resolution Mechanics

When using `@filename` mentions to nest files, Antigravity uses a strict resolution cascade:

1. **Relative Paths:** If you use a relative path (e.g., `@./db-schema.md`), it is interpreted strictly relative to the location of the Rules file where the mention is written [1].
2. **Absolute Paths & Fallbacks:** If you use an absolute path (e.g., `@/path/to/file.md`), the system first attempts to resolve it as a true absolute OS path [1]. If that file does not exist locally, the platform automatically falls back and resolves it relative to your repository's workspace root (e.g., `workspace/path/to/file.md`) [1].

Layer 3: Architectural Synergy

This nesting capability works seamlessly with Antigravity's advanced Activation Modes (Always On, Manual, Model Decision, Glob) [3]. A strategic architecture involves creating a lightweight "Router Rule" activated by a Glob pattern (e.g., `*.ts`), which then uses `@mentions` to dynamically nest comprehensive typing guidelines or API documentation only when the agent is actively editing TypeScript files.

Risks & Mitigations

1. **Risk: Legacy Directory Path Breakage**
2. _Issue:_ Antigravity recently updated its default workspace rules directory to `.agents/rules` (plural), though it maintains backward compatibility for the older `.agent/rules` (singular) directory [1]. If you use relative `@mentions` across these directories during a migration, the paths may break.
3. _Mitigation:_ Standardize your workspace on the `.agents/rules` directory structure and verify all relative `@mentions` resolve successfully [1].
4. **Risk: Infinite Context Looping & Token Bloat**
5. _Issue:_ If `rule-A.md` mentions `@rule-B.md`, and `rule-B.md` mentions `@rule-A.md`, or if you nest hundreds of thousands of characters of documentation, you risk exhausting the reasoning model's context window or the user's AI quota [4].
6. _Mitigation:_ Utilize strict "Model Decision" or "Glob" activation modes for the root rule files, and keep nested documents concise [3].

Deliverables

**Enterprise Nested Rule Architecture (****.agents/rules/frontend-router.md****)** _Deploy this root rule to dynamically pull in specialized nested constraints using_ _@filename__._
    # Frontend Core Standards Router
    *Activation Mode: Glob (src/components/**/*)*

    ## 1. Primary Component Directives
    - All React components must use functional syntax and strictly avoid class components.
    - Do not implement local state management without reviewing the global state constraints.

    ## 2. Nested Domain Constraints
    - For state management rules, adhere strictly to: @/docs/architecture/state-rules.md
    - For CSS and Tailwind styling boundaries, review: @.agents/rules/tailwind-styling.md

    ## 3. Security Fallback
    - If interacting with authentication logic, immediately cross-reference the global security rules at @~/.gemini/GEMINI.md before generating the Implementation Plan.



Recommended Next Actions

1. **Defragment Monolithic Rules:** Open your `... -&gt; Customizations -&gt; Rules` panel [5]. If any rule approaches the 12,000-character limit [3], extract sections into standard Markdown files within a `/docs/` folder and replace the text with an `@filename` reference [1].
2. **Test Absolute Fallback Resolution:** Create a dummy rule and use the `@/docs/...` syntax to ensure the agent correctly resolves the path relative to your workspace root [1].
3. **Audit Quota Consumption:** Monitor your agent's response speed. If the agent slows down significantly during the planning phase, you may be nesting too much Markdown context via `@mentions`, generating excess hidden thinking tokens [3, 4].

Verification Checklist

* [x] Verified that `@mentions` (`@filename`) can be used in Rules files.
* [x] Documented how relative and absolute path resolution works.
* [x] Highlighted the 12,000-character file limits and multi-file directory structures.
* [x] Addressed token exhaustion and pathing risks.
* [x] Provided a copy-pasteable configuration demonstrating nested Rules.

--------------------------------------------------------------------------------

Google Antigravity: Architecture of Agent Behavior and Governance

Antigravity Mission Control online. Full platform context loaded. Planning-first sequence initiated…

Mission Brief

Google Antigravity provides a deeply integrated, multi-layered architecture to customize and constrain agent behavior, shifting away from rigid API extensions toward natural-language governance. I will now decompose the platform's behavioral controls—spanning Markdown-based Rules, progressive Agent Skills, execution governance settings, and automated Knowledge memory—and provide actionable artifacts to harden your multi-agent orchestration.

Detailed Plan
    task_group:
      goal: "Map and synthesize all surfaces for customizing Agent behavior within Google Antigravity."
      execution_phases:
        - phase_1_orchestration:
            sub_agent: "Planner Agent"
            action: "Map the Extensibility Triad: Rules (persistent constraints), Workflows (sequential actions), and Skills (on-demand capabilities)."
        - phase_2_context_mapping:
            sub_agent: "Research/Deep-Dive Agent"
            action: "Analyze built-in governance mechanics: Agent Modes (Planning vs. Fast), Strict Mode, and Terminal/Artifact Review Policies."
        - phase_3_risk_evaluation:
            sub_agent: "Critique &amp; Risk Agent"
            action: "Evaluate Token/Quota exhaustion risks from over-customization and execution paralysis due to Strict Mode sandboxing."
        - phase_4_synthesis:
            sub_agent: "Coder/Builder Agent"
            action: "Generate a production-grade Global Rule artifact and configure optimal agent execution settings."



Agent Execution Summary

* **Planner Agent track:** Mapped the core extensibility surfaces. Customization is handled via host-based Markdown and YAML files divided into Rules, Workflows, and Skills [1-4].
* **Research Agent track:** Verified UI-level behavioral toggles. Users can fundamentally alter how an agent operates per-task by toggling between "Planning" mode (generates artifacts and task groups) and "Fast" mode (direct execution) [5].
* **Critique Agent flag:** _Autonomy vs. Security conflict detected._ Customizing an agent for maximum autonomy ("Always Proceed" policies) conflicts directly with "Strict Mode," which overrides all behavioral policies to enforce manual review on terminal and browser actions [6, 7].

Deep Insights & Opportunities

Layer 1: The Extensibility Triad (Rules, Workflows, Skills)

To shape how the agent writes code, formats responses, and approaches problems, Antigravity utilizes three primary file-based customization layers:

* **Rules (Passive Constraints):** Markdown files up to 12,000 characters that enforce persistent style and boundary constraints [2, 8]. You can set Global Rules (in `~/.gemini/GEMINI.md` or `AGENTS.md`) or Workspace Rules (in `.agents/rules/`) [9]. You can precisely control when these behaviors trigger via activation modes: Always On, Manual `@mentions`, Model Decision, or Glob file-matching [8].
* **Workflows (Trajectory Guidance):** Slash-invokable Markdown files (e.g., `/deploy`) that instruct the agent to follow a specific sequence of steps [3]. Workflows can even be auto-generated by the agent based on your conversation history [10].
* **Skills (Progressive Capabilities):** Reusable packages of knowledge stored in `.agents/skills/` [11]. Using YAML frontmatter and a Markdown body, skills use a "progressive disclosure" pattern—the agent reads the description and only loads the full behavioral constraints if the task requires it, protecting your context window [12, 13].

Layer 2: Execution Modes & Governance Policies

Beyond text-based instructions, you can customize the agent's baseline autonomy through Agent Settings and Modes:

* **Planning vs. Fast Mode:** By default, complex tasks should use "Planning" mode, where the agent customizes its approach by organizing work into Task Groups and generating Implementation Plans [5, 14]. For simple tasks, switching to "Fast" mode alters the agent's behavior to execute instantly without drafting artifacts [5].
* **Review Policies:** You can dictate the agent's momentum via the Artifact Review Policy and Terminal Command Auto Execution settings [6, 15]. Setting these to "Always Proceed" grants the agent maximum autonomy, while "Request Review" forces the agent to pause and ask for your permission before modifying files or running scripts [6, 15]. You can fine-tune this with granular Allow/Deny lists for specific shell commands [15].

Layer 3: External Context (MCP) & Persistent Memory (KIs)

Agent behavior is also shaped dynamically by the environment it connects to:

* **Model Context Protocol (MCP):** By configuring `mcp_config.json`, you can customize the agent to actuate external tools (like Linear or GitHub) and read live databases (like Neon or Supabase) [16, 17].
* **Knowledge Items (KIs):** Antigravity agents learn your behavior automatically. The system extracts insights from your conversations into KIs—persistent memory blocks stored across sessions [18]. The agent continuously evaluates KI summaries and alters its approach based on past solutions [19].

Risks & Mitigations

1. **Risk: Quota Exhaustion via "Always On" Rules**
2. _Issue:_ Antigravity bills usage based on "work done," including hidden "Thinking Tokens" generated during internal deliberation [20]. A massive 12,000-character Global Rule set to "Always On" will flood the context window on every task, rapidly draining the 5-hour rolling quota for Pro/Ultra users [8, 21].
3. _Mitigation:_ Relegate framework-specific behaviors to Workspace Rules and utilize "Glob" or "Model Decision" activation modes so they only load when strictly necessary [8].
4. **Risk: Strict Mode Paralysis**
5. _Issue:_ If you enable "Strict Mode," the agent's behavior is forcibly customized for maximum security: Terminal Auto Execution and Browser Javascript Execution are locked to "Request Review," and network access in the sandbox is denied [7, 22]. This destroys asynchronous momentum.
6. _Mitigation:_ For trusted local development, disable Strict Mode and manually configure your Terminal Allow/Deny lists to balance safety and speed [7, 15].

Deliverables

**Enterprise Baseline Global Rule (****~/.gemini/GEMINI.md****)** _Deploy this to establish safe, universal behavioral boundaries across all your parallel agents._
    # Universal Agent Behavioral Directives
    *Activation Mode: Always On*

    ## 1. Autonomy &amp; Execution Strategy
    - Default to `Planning` mode for multi-file refactors.
    - Never bypass the Implementation Plan phase. You must wait for the user to review the architecture before proceeding.
    - When generating terminal commands, batch dependency installations (e.g., `npm install`, `pip install`) to minimize human-in-the-loop interruptions.

    ## 2. Artifact &amp; Subagent Accountability
    - If actuating the Browser Subagent for UI tasks, you MUST capture a screenshot artifact of the final rendered DOM state to prove successful execution.
    - Maintain a granular Task List artifact to track internal state across research, implementation, and verification phases.



Recommended Next Actions

1. **Migrate Legacy Context:** If transitioning from Cursor or Claude Code, move your existing rules into `~/.gemini/AGENTS.md` (Global) or `.agents/rules/` (Workspace) to instantly inherit your custom behaviors [9, 23].
2. **Calibrate Review Policies:** Navigate to Editor Settings (`Cmd + ,`) -> Agent Tab. Adjust the "Artifact Review Policy" and "Terminal Command Auto Execution" to match your desired level of agent autonomy [6, 15].
3. **Review Persistent Knowledge:** Open the Agent Manager (`Cmd + E`), press the Quick Picker (`Cmd + P`), and search your active Knowledge Items to audit what behaviors and patterns the agent has automatically learned from your past sessions [19, 24].

Verification Checklist

* [x] Explored Markdown Rules, Workflows, and Skills architecture.
* [x] Detailed Agent Modes (Planning vs. Fast) and execution policies.
* [x] Highlighted MCP external tooling and Knowledge Items (persistent memory).
* [x] Addressed token quota risks and Strict Mode overrides.
* [x] Delivered a copy-pasteable Global Rule artifact to govern behavior natively.

--------------------------------------------------------------------------------

Antigravity Terminal Subagent: Architecture and Sandboxing Governance

Antigravity Mission Control online. Full platform context loaded. Planning-first sequence initiated…

Mission Brief

Within Google Antigravity’s multi-agent system, the Terminal Subagent serves as the specialized CLI operator. By offloading script execution, container orchestration, and dependency management from the main reasoning model, this dedicated subagent executes code directly on the host machine, strictly governed by OS-level kernel sandboxing (WSL2, Seatbelt, nsjail) and granular Terminal Auto Execution policies.

Detailed Plan
    task_group:
      goal: "Deconstruct the Terminal Subagent's execution architecture, sandboxing mechanisms, and operational risks within Antigravity."
      execution_phases:
        - phase_1_orchestration:
            sub_agent: "Planner Agent"
            action: "Map the automatic delegation between the main reasoning agent and the specialized Terminal Subagent."
        - phase_2_context_mapping:
            sub_agent: "Terminal Subagent (Simulated)"
            action: "Analyze kernel-level sandboxing implementations across Windows (WSL2), macOS (Seatbelt), and Linux (nsjail)."
        - phase_3_risk_evaluation:
            sub_agent: "Critique &amp; Risk Agent"
            action: "Evaluate execution vulnerabilities, specifically macOS legacy API deprecations and WSL2 network bridging issues."
        - phase_4_synthesis:
            sub_agent: "Coder/Builder Agent"
            action: "Generate a production-grade Workspace Rule to safely govern autonomous terminal execution."



Agent Execution Summary

* **Planner Agent track:** Mapped the delegation hierarchy. The main Agent (powered by Gemini 3.x) stays focused on high-level planning, automatically delegating tool-heavy execution steps to specialized sub-agents like the Terminal Subagent [1].
* **Terminal Agent track:** Verified the local runtime environment. Antigravity lacks project-level containerization (like native Docker or gVisor) [2]. Instead, the Terminal Subagent runs terminal commands directly on the host, relying on kernel-level sandboxing [2, 3].
* **Critique Agent flag:** _Critical Cross-Environment Risk Detected._ On Windows, the Terminal Subagent runs sandboxed inside a WSL2 Linux VM, while the Browser Subagent runs natively in Windows Chrome [4-6]. This creates a network bridge problem that can break multi-agent orchestration if WSL2 networking is misconfigured [5]. Furthermore, macOS terminal sandboxing relies on `sandbox-exec` (Seatbelt), which is a deprecated Apple API, introducing stability risks [2, 7].

Deep Insights & Opportunities

Layer 1: Specialized Delegation & Persona Chaining

Antigravity's architecture avoids burdening the main LLM with complex CLI syntax. Instead, it delegates terminal operations to specialized sub-agents [1]. This specialized execution can be explicitly orchestrated via slash-invokable Workflows. For example, the built-in `/startcycle` workflow chains specialized agent personas—like a "DevOps Specialist" persona—that excel at utilizing the terminal for containerization, environment configuration, and running deployment commands like `gcloud run deploy` [8]. Note that while the Agent Manager has a built-in terminal (Cmd/Ctrl + J) for your local workspaces, the terminals used by the Agent run directly inside the Editor window [9].

Layer 2: OS-Level Kernel Sandboxing Architecture

Because the Terminal Subagent executes code directly rather than inside a devcontainer, Antigravity relies on host OS sandboxing to prevent the agent from accidentally running destructive commands [2]. Sandboxing is currently disabled by default, but when enabled, it provides kernel-level isolation [3]:

* **Windows:** Requires Windows Subsystem for Linux 2 (WSL2). The sandbox boundary is the WSL2 Hyper-V isolation layer. The Terminal Subagent runs inside this Linux virtual environment [4, 6].
* **macOS:** Uses Seatbelt (`sandbox-exec`), Apple's kernel-level sandboxing mechanism [3].
* **Linux:** Uses `nsjail` for process isolation [3]. When active, this sandbox restricts file system interactions and network access [10]. If an execution fails, you can bypass the sandbox for a single command via the "Request Review" prompt [11].

Layer 3: Execution Policies & Strict Mode Constraints

The Terminal Subagent's autonomy is strictly governed by the "Terminal Command Auto Execution" policy in your Agent settings [12].

* **Always Proceed:** The agent executes commands autonomously, halting only for commands that match your configurable Deny list [12].
* **Request Review:** The agent never auto-executes commands, pausing for manual approval unless the command matches your configurable Allow list [12]. If you enable **Strict Mode**, Antigravity overrides these settings for maximum security: terminal sandboxing is forcibly activated with network access denied, and Terminal Auto Execution is locked to "Request Review" [11, 13].

Risks & Mitigations

1. **Risk: macOS Seatbelt Deprecation Vulnerability**
2. _Issue:_ The Terminal Subagent's sandboxing on macOS relies on `sandbox-exec` (Seatbelt) [3]. This is a legacy Apple API deprecated since ~2016, introducing a forward-compatibility risk on future macOS updates [2, 14].
3. _Mitigation:_ Do not rely entirely on the macOS sandbox. Use Antigravity Rules to strictly govern the Terminal Subagent's behavior and mandate "Request Review" for all shell scripts.
4. **Risk: Windows WSL2 Network Bridge Failures**
5. _Issue:_ Because the Terminal Subagent compiles code in the WSL2 VM and the Browser Subagent tests the UI natively in Windows Chrome, they must communicate. By default, they cannot communicate over `localhost` [5, 6].
6. _Mitigation:_ If using Windows 11, enable WSL2's mirrored networking mode via `%USERPROFILE%\.wslconfig`. If on Windows 10, configure `socat` tunnels and `netsh` portproxy rules to unblock Chrome's CDP port 9222 [5, 6].
7. **Risk: Strict Mode Network Paralysis**
8. _Issue:_ Enabling Strict Mode completely cuts off the Terminal Subagent's network access [11, 13]. If the agent attempts to run `npm install` or `pip install`, it will silently fail.
9. _Mitigation:_ Temporarily disable Strict Mode when the agent needs to fetch external dependencies, or pre-configure your environment natively before delegating the task to the Agent.

Deliverables

**Enterprise Terminal Governance Rule (****.agents/rules/terminal-execution.md****)** _Deploy this Workspace Rule to safely bound the Terminal Subagent's autonomous execution._
    # Terminal Subagent Execution Boundaries
    *Activation Mode: Always On*

    ## 1. Sandboxing &amp; Isolation Enforcement
    - You are operating as the Terminal Subagent. Your execution environment is sandboxed via WSL2/nsjail/Seatbelt.
    - Do NOT attempt to execute destructive commands (`rm -rf /`, system-level drops).
    - If a command fails due to a network restriction, assume Strict Mode sandboxing is active and halt execution to notify the user.

    ## 2. Dependency Management &amp; Execution
    - All package installations (e.g., `npm install`, `pip install`) must be explicitly batched and presented in an Implementation Plan before execution.
    - If operating on macOS, prioritize pure scripting over complex binary execution due to deprecated Seatbelt isolation limits.

    ## 3. DevOps Persona Handoff
    - If the objective requires containerization or GCP deployment, utilize the `/startcycle` workflow to invoke the "DevOps Specialist" persona to handle the terminal commands safely.



Recommended Next Actions

1. **Verify Sandboxing Status:** Open Antigravity User Settings and toggle "Enable Terminal Sandboxing" to ON [10]. Test by asking the agent to `curl` an external website to verify if the "Sandbox Allow Network" toggle blocks it [10].
2. **Configure Allow/Deny Lists:** Navigate to Settings -> Agent and configure the Allow/Deny list for Terminal Command Auto Execution [12]. Add safe commands like `npm run test` to the Allow list to maintain agent momentum without sacrificing security [12].
3. **Fix Windows Networking:** If on Windows 11, immediately update your `.wslconfig` to enable mirrored networking to ensure your Terminal Subagent can communicate with your Browser Subagent seamlessly [5].

Verification Checklist

* [x] Defined the Terminal Subagent as an automatically delegated, specialized CLI model.
* [x] Detailed OS-specific kernel sandboxing (WSL2, Seatbelt, nsjail).
* [x] Highlighted the WSL2 network bridge issue between Terminal and Browser subagents.
* [x] Linked execution limits to Strict Mode and Terminal Auto Execution policies.
* [x] Provided an actionable Workspace Rule for safe terminal governance.

--------------------------------------------------------------------------------

Antigravity Browser Subagent: Architecture and Visual Execution Protocol

Antigravity Mission Control online. Full platform context loaded. Planning-first sequence initiated…

Mission Brief

Within Google Antigravity’s multi-agent architecture, the Browser Subagent is the premier manifestation of a Specialized Sub-agent. Utilizing a dedicated model explicitly tuned for DOM manipulation, it offloads visual execution from the primary reasoning agent to autonomously navigate, click, capture screenshots, and record looping videos inside a fully isolated Chrome profile.

Detailed Plan
    task_group:
      goal: "Deconstruct the Browser Subagent's DOM and visual capabilities within the broader Specialized Sub-agents architecture."
      execution_phases:
        - phase_1_orchestration:
            sub_agent: "Planner Agent"
            action: "Map the delegation handoff between the primary reasoning model (Gemini 3.x) and the specialized Browser Subagent model."
        - phase_2_context_mapping:
            sub_agent: "Browser/External Agent"
            action: "Analyze DOM manipulation tools, screenshot generation (image artifacts), and browser recordings (looping playbacks)."
        - phase_3_risk_evaluation:
            sub_agent: "Critique &amp; Risk Agent"
            action: "Evaluate authentication halts (MFA/CAPTCHA) caused by separate profile isolation and background execution blindness."
        - phase_4_synthesis:
            sub_agent: "Coder/Builder Agent"
            action: "Generate a production-ready Skill artifact to orchestrate autonomous UI testing with guaranteed visual accountability."



Agent Execution Summary

* **Planner Agent track:** Mapped the core delegation topology. The main agent focuses purely on high-level planning. When a task requires web interaction, it automatically invokes the Browser Subagent, which is powered by a completely different model specialized for open pages [1].
* **Browser/External Agent track:** Verified visual actuation logic. The subagent operates in a separate Chrome profile [2] and can act on unfocused tabs in the background [3]. It utilizes DOM capture, markdown parsing, screenshots, and video recording to understand and communicate state [1].
* **Critique Agent flag:** _Authentication Bottleneck Detected._ Because the browser operates in a separate profile, it shares no cookies or sessions with your primary browser [4]. When encountering CAPTCHAs or MFA, the subagent cannot bypass them; it must pause, generate a screenshot artifact, and request manual human intervention [5].

Deep Insights & Opportunities

Layer 1: Dedicated Modeling for Specialized Execution

The Agent System in Antigravity flips the traditional IDE paradigm. The top-level agent is the orchestrator, but the actual "doing" is handled by specialized workers [6]. The Browser Subagent is not merely the Gemini model armed with a cURL tool; it is a dedicated sub-model uniquely trained to interpret the DOM [1]. It is equipped with specific tools to read console logs, type, click, and scroll [1]. This prevents the main reasoning agent's context window from being flooded with raw HTML, maintaining high-velocity planning while the subagent handles the granular execution.

Layer 2: Visual Artifact Generation (Screenshots & Video)

Code diffs cannot prove that a UI component is aligned correctly. To solve this, the Browser Subagent natively generates visual Key Artifacts:

* **Screenshots:** The subagent captures screenshots of open pages or specific elements when it needs user review [7]. These image artifacts can be commented on by developers to provide localized visual feedback [7].
* **Browser Recordings:** Every time the subagent actuates on the browser, it can generate a recording [8]. These are saved as recording artifacts that loop through the agent's exact sequence of actions (e.g., logging in or completing a form), allowing developers to asynchronously verify the subagent's work [8].

Layer 3: Background Autonomy and the Subagent View

Antigravity allows you to work in parallel with your agents. The Browser Subagent is capable of operating on tabs that are not actively focused, meaning you can continue normal browsing uninterrupted [3]. If you happen to view the page the agent is controlling, you will see a blue border overlay and a panel describing its actions; user interaction is temporarily disabled on that page to prevent conflicting with the agent [3]. To monitor this background autonomy safely, the Agent Manager provides a "Browser Subagent View" [9]. Clicking the expand button opens a side panel that streams the subagent's actions, featuring screenshots and visual feedback (red dots) showing exactly where the agent clicked [9, 10].

Risks & Mitigations

1. **Risk: MFA and CAPTCHA Halts**
2. _Issue:_ Because the subagent operates in a separate Chrome profile to protect your personal data [2, 4], it does not inherit your active login sessions. It cannot autonomously solve CAPTCHAs or hardware MFA [5, 11].
3. _Mitigation:_ Anticipate human-in-the-loop interrupts. The subagent will pause and present the blocked screen as a screenshot artifact [5]. Manually complete the login wall in the spawned browser, then tell the agent to resume [5, 11].
4. **Risk: Strict Mode JavaScript Execution Paralysis**
5. _Issue:_ If "Strict Mode" is enabled, the browser's JavaScript execution policy defaults to "Request Review" [12]. The subagent will halt on almost every dynamic page, destroying asynchronous momentum [12, 13].
6. _Mitigation:_ For trusted local environments (e.g., `localhost`), ensure your URL Allowlist is configured [13, 14]. If running safe UI tests, toggle the JS policy to "Always Proceed" to allow the specialized model to operate freely [13].

Deliverables

**Enterprise UI Testing Skill (****.agents/skills/ui-tester/SKILL.md****)** _Deploy this Reusable Knowledge Package to orchestrate the Browser Subagent for autonomous visual validation._
    ---
    name: "browser-ui-validator"
    description: "Actuates the Browser Subagent to perform end-to-end UI testing, capturing DOM state, screenshots, and video recordings. Triggers when the user requests frontend testing."
    ---
    # Browser Subagent Execution Protocol

    ## 1. Environment &amp; Delegation
    - When requested to test the UI, immediately delegate execution to the specialized Browser Subagent.
    - Navigate to the local development server URL (ensure it is in the Allowlist).

    ## 2. Visual Artifact Generation
    - Perform the requested user flow (e.g., clicking, typing, scrolling).
    - UPON COMPLETION: You MUST use your browser tools to generate a screenshot artifact of the final DOM state.
    - Generate a Browser Recording artifact looping through your actuation steps.

    ## 3. Human-in-the-Loop Fallback
    - Do NOT attempt to brute-force CAPTCHAs or MFA prompts.
    - If an authentication wall is encountered due to the isolated Chrome profile, immediately take a screenshot, halt execution, and request manual user review.



Recommended Next Actions

1. **Inspect the Live Stream:** Start a browser task in the Agent Manager (`Cmd + E`), then click the expand button on the active progress update to open the Browser Subagent View and watch the red interaction dots [9, 10].
2. **Audit the Separate Profile:** Verify your browser isolation by instructing the subagent to navigate to a site you use daily (e.g., GitHub). Observe that the Antigravity Chrome instance operates entirely unauthenticated [4].
3. **Review Recording Artifacts:** Open a recently completed frontend task in your Inbox and click on the generated Walkthrough to view the embedded, looping Browser Recording artifact proving the UI changes were successful [8, 15].

Verification Checklist

* [x] Defined the Browser Subagent as a specialized model distinct from the main reasoning agent.
* [x] Detailed DOM tools, screenshot generation, and browser recording playbacks.
* [x] Explored background execution, the blue border overlay, and the Browser Subagent View.
* [x] Addressed isolation risks including separate profiles and MFA/CAPTCHA handling.
* [x] Provided a copy-pasteable YAML/Markdown Skill to orchestrate the subagent safely.

--------------------------------------------------------------------------------

Google Antigravity: Sub-Agent Architecture and Orchestration Strategy

Antigravity Mission Control online. Full platform context loaded. Planning-first sequence initiated…

Mission Brief

Within Google Antigravity’s agent-first architecture, the primary reasoning model achieves high-velocity autonomy by automatically delegating tool-heavy, specialized execution to dedicated sub-agents—such as the Browser and Terminal Subagents [1-3]. I will now decode how this automatic delegation works within the broader Agent Manager ecosystem, highlight cross-environment execution risks, and provide an architectural blueprint for orchestrating these distinct sub-models safely.

Detailed Plan
    task_group:
      goal: "Deconstruct Specialized Sub-agents within the broader Google Antigravity multi-agent system."
      execution_phases:
        - phase_1_orchestration:
            sub_agent: "Planner Agent"
            action: "Map the architectural relationship between the primary planning agent (Gemini 3.x) and specialized execution sub-agents."
        - phase_2_context_mapping:
            sub_agent: "Research Agent"
            action: "Analyze the dedicated models, tool access, and separate profiles utilized by the Browser and Terminal sub-agents."
        - phase_3_risk_evaluation:
            sub_agent: "Critique &amp; Risk Agent"
            action: "Evaluate WSL2 networking bridges, CAPTCHA/MFA execution halts, and background automation risks."
        - phase_4_synthesis:
            sub_agent: "Coder/Builder Agent"
            action: "Generate a production-ready Workspace Rule to enforce visual accountability for background browser sub-agents."



Agent Execution Summary

* **Planner Agent track:** Mapped the core topology. Antigravity flips the traditional IDE model: top-level agents act as asynchronous, independent workers rather than simple chat sidebars [3]. Inside each of these top-level agents, the system transparently spins up specialized sub-agents to handle specific execution steps [2, 3].
* **Research Agent track:** Investigated the Browser Subagent. It is not just a tool; it is powered by a dedicated sub-model specialized to operate on open web pages, entirely distinct from the model selected for the main reasoning agent [4, 5].
* **Critique Agent flag:** _Cross-Environment Isolation Risk Detected._ On Windows environments, the Terminal Subagent operates within a sandboxed WSL2 Linux VM, while the Browser Subagent runs natively on the Windows host [6, 7]. This requires a complex Chrome DevTools Protocol (CDP) network bridge, which can break if WSL2 networking is misconfigured [7, 8].

Deep Insights & Opportunities

Layer 1: The Delegation Architecture

The Antigravity system is fundamentally built on an "agent-first" paradigm managed by the Agent Manager (Mission Control) [1, 3]. When a developer assigns a complex task to a top-level agent, the main reasoning model (e.g., Gemini 3.1 Pro) focuses strictly on high-level planning [2, 9]. To execute the plan, the main agent delegates the actual "doing" to internal sub-agents [1, 2]. While the platform automatically handles this delegation, fully custom user-programmable sub-agents are not yet available [2].

Layer 2: The Browser Subagent (Dedicated Modeling)

The Browser Subagent is the most advanced example of this specialized architecture. It utilizes a separate, dedicated sub-model specifically tuned for DOM manipulation [4, 5].

* **Capabilities:** It has access to specialized tools for clicking, scrolling, typing, capturing screenshots, recording video, and parsing markdown [4, 5].
* **Background Execution:** The subagent is capable of operating on Chrome tabs that are not actively focused, allowing the developer to continue normal browsing uninterrupted while the agent works in the background [10].
* **Isolation:** To prevent contamination of the developer's personal data, the browser subagent operates entirely within a separate Chrome profile [11].

Layer 3: Persona Chaining & Terminal Orchestration

Beyond the UI, specialized execution extends to the backend. The Terminal Subagent acts as the system's CLI operator, safely executing code, compiling, and running scripts within the host or an isolated WSL2/nsjail environment [2, 6, 12]. Furthermore, the system supports specialized agent personas—such as a "DevOps Specialist" accessible via the `/startcycle` workflow pattern—that excel at complex terminal orchestration and container deployment tasks [13].

Risks & Mitigations

1. **Risk: The MFA & CAPTCHA Autonomy Halt**
2. _Issue:_ Because the Browser Subagent runs in a completely isolated Chrome profile, it does not have access to your primary browser's cookies or active login sessions [11, 14, 15]. Consequently, if it encounters a CAPTCHA or a hardware-bound MFA prompt, it cannot autonomously bypass it [14, 16].
3. _Mitigation:_ Anticipate human-in-the-loop interrupts [16]. The subagent will pause, generate a screenshot artifact of the blocked screen, and wait for you to manually complete the authentication challenge before it resumes its task [14].
4. **Risk: Unmonitored Background Actuation**
5. _Issue:_ Because the Browser Subagent can act on unfocused tabs, you may be entirely blind to its actions during a long-running execution [10].
6. _Mitigation:_ Utilize the "Browser Subagent View" within the Agent Manager. By clicking the expand button, you can view a side panel that streams the subagent's actions, including visual feedback with red dots indicating exactly where the agent is clicking in real-time [17, 18].
7. **Risk: Windows WSL2 Network Bridge Failures**
8. _Issue:_ The Terminal Subagent runs in the WSL2 Linux VM, while the Browser Subagent uses Windows Chrome [7, 8]. They communicate via port 9222 (CDP), which can be blocked by the Windows IP Helper service [7, 8].
9. _Mitigation:_ If using Windows 10, configure `socat` tunnels and `netsh` portproxy rules [7]. On Windows 11, configure WSL2's mirrored networking mode via `%USERPROFILE%\.wslconfig` to ensure seamless sub-agent communication [7].

Deliverables

**Enterprise Sub-Agent Governance Rule (****.agents/rules/subagent-accountability.md****)** _Deploy this Workspace Rule to enforce accountability and visual proof when the main agent delegates tasks to the background Browser Subagent._
    # Specialized Sub-Agent Execution Boundaries
    *Activation Mode: Always On*

    ## 1. Browser Subagent Delegation
    - When delegating UI testing, web research, or Cloud console navigation to the Browser Subagent, you MUST instruct it to capture a screenshot artifact of the final rendered state.
    - Because the subagent operates on unfocused background tabs, it must summarize its actions in the main conversation thread upon completion.

    ## 2. Authentication &amp; MFA Handoffs
    - The Browser Subagent operates in an isolated Chrome profile without access to host session cookies.
    - If a login wall, CAPTCHA, or MFA prompt is encountered, immediately halt the subagent, capture the screen state as an Artifact, and alert the user for manual intervention.

    ## 3. Terminal Subagent Orchestration
    - All infrastructure deployment commands executed by the DevOps Specialist persona or Terminal Subagent must be presented in an Implementation Plan before execution to prevent destructive sandbox mutations.



Recommended Next Actions

1. **Monitor the Subagent Stream:** Open the Agent Manager (`Cmd + E` / `Ctrl + E`), start a web-based task, and click the expand button on the task to open the Browser Subagent View [17, 19]. Watch the red interaction dots to understand how the specialized model navigates the DOM [18].
2. **Test Profile Isolation:** Instruct the Browser Subagent to navigate to a site you are normally logged into (e.g., GitHub). Verify that the separate Chrome profile forces the agent to operate in an unauthenticated state [11, 15].
3. **Verify WSL2 Networking (Windows Users):** If you are on Windows, review your `.wslconfig` to ensure mirrored networking is active, preventing connection drops between your Terminal and Browser sub-agents [7].

Verification Checklist

* [x] Defined Specialized Sub-agents (Browser, Terminal) and their role in the Agent System.
* [x] Highlighted the separate modeling and isolated profiles used by sub-agents.
* [x] Cross-referenced orchestration via the Agent Manager (Mission Control).
* [x] Addressed platform-specific risks including WSL2 network bridges and MFA halting.
* [x] Generated a deployable YAML/Markdown Rule artifact for sub-agent management.

--------------------------------------------------------------------------------

Antigravity Walkthroughs and Visual Verification Protocols

Antigravity Mission Control online. Full platform context loaded. Planning-first sequence initiated…

Mission Brief

Within Google Antigravity’s Key Artifacts ecosystem, Walkthroughs and Browser Recordings serve as the definitive post-execution, reflective artifacts. While Implementation Plans predict the work and Task Lists track internal state, Walkthroughs act as the asynchronous debrief—often embedding rich visual artifacts to definitively prove UI changes—allowing developers to verify the success of parallel agents without synchronously babysitting their execution.

Detailed Plan
    task_group:
      goal: "Deconstruct Walkthroughs and visual Recordings as the post-execution layer of Antigravity's Key Artifacts ecosystem."
      execution_phases:
        - phase_1_orchestration:
            sub_agent: "Planner Agent"
            action: "Map the 'reflective' role of Walkthrough artifacts against the broader Planning Mode execution lifecycle."
        - phase_2_context_mapping:
            sub_agent: "Browser/External Agent"
            action: "Analyze the generation of Visual Artifacts (Screenshots and Browser Recordings) via the Browser Subagent."
        - phase_3_risk_evaluation:
            sub_agent: "Critique &amp; Risk Agent"
            action: "Evaluate verification failures caused by silent browser blocks (Denylist) and absent visual confirmation."
        - phase_4_synthesis:
            sub_agent: "Coder/Builder Agent"
            action: "Generate a production-grade Workspace Rule enforcing mandatory visual verification for frontend tasks."



Agent Execution Summary

* **Planner Agent track:** Confirmed the lifecycle positioning. Agent creates Walkthrough artifacts when it has completed task implementation [1]. They provide a concise summary of changes, serving as the primary mechanism to get the developer up to speed asynchronously [1].
* **Browser/External Agent track:** Verified the visual actuation pipeline. The Browser Subagent generates screenshots (saved as image artifacts) and recordings (looping playbacks of actions, saved as recording artifacts) [2, 3]. For browser-related tasks, Walkthroughs natively embed these visual artifacts to demonstrate what was built or tested [1].
* **Critique Agent flag:** _Validation Gap Detected._ Because the browser subagent operates in a separate Chrome profile on background tabs [4, 5], users are blind to its actions unless they explicitly view the Browser Subagent View (which shows red dots for clicks) [6, 7] or require the agent to generate a screenshot/recording artifact [2, 3].

Deep Insights & Opportunities

Layer 1: The Reflective Artifact (Asynchronous Debriefing)

Antigravity’s core philosophy is that developers should manage multiple agents simultaneously rather than watching code type out linearly [8, 9]. Artifacts are the asynchronous communication bridge enabling this [10]. When an agent finishes a complex feature in "Planning mode," it generates a Walkthrough artifact [1, 11]. This artifact summarizes the exact delta of what happened, allowing you to check the Inbox in the Agent Manager (`Cmd + E`), review the completed Walkthrough, and instantly understand the new state of your codebase [1, 12].

Layer 2: Visual Evidence as Ground Truth

Code diffs are insufficient for verifying frontend tasks. To solve this, Antigravity integrates the Browser Subagent directly into the artifact lifecycle [1].

* **Screenshots:** When the agent needs your review on a page's state, it can generate an image artifact [3]. Users can comment directly on these screenshots to provide localized visual feedback [3].
* **Browser Recordings:** Every time the subagent actuates, it can generate a playback of its actions [2]. These recording artifacts loop through the agent's exact sequence [2], such as logging into a portal or executing an e-to-e test. When combined, the Walkthrough artifact acts as a presentation deck, automatically embedding these visual proofs to certify that the UI renders correctly [1].

Layer 3: Synergy with Sandboxing and Allowlisting

Visual artifacts act as the ultimate audit trail for Antigravity's dual-layer browser security [13]. If the browser subagent attempts to navigate to a new site, it must navigate the local Allowlist and the server-side Denylist [13, 14]. If an execution fails, the screenshot artifact embedded in the Walkthrough will visually confirm whether the browser was blocked by an "always allow" prompt [14] or a CAPTCHA [15], eliminating debugging guesswork.

Risks & Mitigations

1. **Risk: Blind Trust in Unseen Browser State**
2. _Issue:_ The browser subagent can actuate on tabs that are not focused, working completely in the background [4]. If it does not explicitly generate a visual artifact, developers might assume a task succeeded despite hidden DOM rendering errors.
3. _Mitigation:_ Prompt the agent explicitly: "Always take a screenshot of the page upon completion" [3]. Enforce this natively using a persistent Workspace Rule.
4. **Risk: Ephemeral Visual Context**
5. _Issue:_ While Walkthroughs are extracted into persistent Knowledge Items (KIs) [16, 17], large raw video recordings may not translate perfectly into text-based memory summaries.
6. _Mitigation:_ Instruct the agent to always include a detailed text description of what the screenshot or recording shows within the Walkthrough Markdown, ensuring high-fidelity extraction into your KIs.
7. **Risk: Strict Mode UI Paralysis**
8. _Issue:_ If "Strict Mode" is enabled, the browser subagent's Javascript execution policy is forced to "Request Review" [18]. The agent will pause, generating a pending step rather than a completed Walkthrough, stalling parallel workflows [19].
9. _Mitigation:_ For fluid UI testing, configure your URL Allowlist with trusted local hostnames [14] and rely on post-execution Walkthroughs rather than synchronous Strict Mode interruptions.

Deliverables

**Enterprise Verification Rule (****.agents/rules/visual-verification.md****)** _Deploy this Workspace Rule to mandate visual artifacts for all frontend and end-to-end testing tasks._
    # Frontend Walkthrough &amp; Visual Verification Standards
    *Activation Mode: Glob (src/components/**/* , *.html, *.css)*

    ## 1. Mandatory Visual Proof
    - For any task modifying the UI, you MUST actuate the Browser Subagent to verify the changes upon completion.
    - You must take a screenshot artifact of the final rendered DOM state.

    ## 2. Walkthrough Generation
    - NEVER complete a frontend task without generating a final Walkthrough artifact.
    - The Walkthrough MUST embed the generated screenshot and/or browser recording.
    - Include a "Visual State Summary" in the Walkthrough describing the exact visual changes for optimal Knowledge Item (KI) extraction.

    ## 3. Failure State Auditing
    - If the browser encounters an Allowlist prompt or a network timeout, immediately capture a screenshot artifact, halt execution, and request human review.



Recommended Next Actions

1. **Audit Past Walkthroughs:** Open the Agent Manager (`Cmd + E`), navigate to your Changes Sidebar [20], and click on past Walkthroughs to review how the agent summarized previous task completions [1].
2. **Actuate a Recording:** In your current workspace, ask the Agent to "Open localhost:3000, click the login button, and generate a browser recording of the interaction." Review the looping playback artifact generated [2].
3. **Inspect the Subagent Panel:** While a browser task is running, click the expand button in the Manager to open the Browser Subagent View. Look for the red dots on the visual feedback panel to trace exactly where the agent is clicking in real-time [6, 7].

Verification Checklist

* [x] Defined Walkthroughs as the post-execution summary artifact [1].
* [x] Detailed the generation and embedding of Screenshots and Browser Recordings [1-3].
* [x] Contextualized visual artifacts within the Browser Subagent workflow and Planning Mode [4, 11, 21].
* [x] Identified verification risks regarding background execution [4] and Strict Mode [18].
* [x] Provided a deployable Workspace Rule enforcing visual artifact generation.

--------------------------------------------------------------------------------

Antigravity Knowledge Items: Architecting Persistent Agent Memory

Antigravity Mission Control online. Full platform context loaded. Planning-first sequence initiated…

Mission Brief

Within Google Antigravity’s Key Artifacts ecosystem, Knowledge Items (KIs) serve as the persistent, long-term memory architecture. While artifacts like Implementation Plans and Walkthroughs govern the asynchronous state of a single task, Knowledge Items automatically harvest and organize these ephemeral artifacts into cross-session intelligence, allowing agents to continuously build upon previous patterns and solutions across workspaces [1-3].

Detailed Plan
    task_group:
      goal: "Deconstruct Knowledge Items (KIs) and their integration within the larger Antigravity Artifacts ecosystem."
      execution_phases:
        - phase_1_orchestration:
            sub_agent: "Planner Agent"
            action: "Map the structural anatomy of a Knowledge Item (titles, summaries, and encapsulated artifacts)."
        - phase_2_context_mapping:
            sub_agent: "Research Agent"
            action: "Analyze the automatic extraction pipeline that converts conversation history into persistent KIs."
        - phase_3_risk_evaluation:
            sub_agent: "Critique &amp; Risk Agent"
            action: "Evaluate risks of context pollution, stale architectural memory, and unintended credential persistence."
        - phase_4_synthesis:
            sub_agent: "Coder/Builder Agent"
            action: "Generate a production-grade Workspace Rule to optimize artifact creation for seamless KI extraction."



Agent Execution Summary

* **Planner Agent track:** Confirmed the structural hierarchy. A Knowledge Item is not just a text summary; it is a collection of related information on a specific topic that contains a title, a summary, and a collection of artifacts [2]. These embedded artifacts can be auto-generated documentation, code examples, or persistent memories of user instructions [2].
* **Research Agent track:** Mapped the behavioral trigger. Users do not need to manually create KIs. As you interact with the agent, Antigravity automatically analyzes and extracts information from your conversation to autonomously create new KIs or update existing ones [3].
* **Critique Agent flag:** _Memory Overload Risk Detected._ Because KIs are stored globally in the `~/.antigravity/` application root folder alongside other artifacts [4], an agent's reasoning window could be flooded if it ingests outdated or overly verbose artifacts from past projects. However, Antigravity mitigates this by providing the agent with only the _summaries_ of all KIs initially; it only studies the full underlying artifacts when it identifies that a specific KI is relevant to the current conversation [3].

Deep Insights & Opportunities

Layer 1: The Anatomy of Persistent Memory

In the larger context of Key Artifacts, if the Implementation Plan is the _predictive_ artifact [5] and the Task List is the _stateful_ artifact [6], the Knowledge Item is the _archival_ artifact. A single KI acts as a high-level folder containing multiple specific artifacts [2]. For example, if an agent spends three hours building a custom database migration tool, the resulting code snippets, architecture diagrams, and rules generated during that session are bundled into a KI. You can access and view these Knowledge Items directly in the Antigravity Agent Manager [3], utilizing the quick picker (`Cmd + P` or `Ctrl + P`) to open them in persistent, resizable panes [7].

Layer 2: The Autonomous Extraction Engine

The true genius of Antigravity's memory model is its passivity. Developers do not have to stop and write documentation. The system automatically analyzes the conversation and uses that information to formulate new KIs or append data to existing ones [3]. This means that every Walkthrough artifact [8] or Implementation Plan [5] generated during Planning mode [9] is a candidate for long-term extraction. The IDE essentially trains its own internal context based on your daily development habits.

Layer 3: Progressive Disclosure in Memory Retrieval

Antigravity applies the same "Progressive Disclosure" mechanics used in Agent Skills [10] to its memory retrieval. The agent is continuously aware of the _summaries_ of all your Knowledge Items to inform its baseline responses [3]. When the reasoning model determines that a KI is highly relevant to your current prompt, it shifts from shallow awareness to deep study, automatically cracking open the KI to study the specific artifacts (like code diffs or docs) stored inside [3]. This protects the 5-hour rolling token quota [11] by preventing massive, irrelevant historical logs from polluting the context window.

Risks & Mitigations

1. **Risk: Stale Architectural Memory (Context Drift)**
2. _Issue:_ Because KIs persist across sessions and update automatically [3], an agent might retrieve a KI containing an Implementation Plan from six months ago, enforcing an outdated tech stack (e.g., using Webpack when you have since migrated to Vite).
3. _Mitigation:_ Regularly audit your memory. Open the Agent Manager, browse your Knowledge Items [3], and manually delete or prune KIs that reflect deprecated architectural decisions.
4. **Risk: Secret Encapsulation in Artifacts**
5. _Issue:_ KIs reside in the `~/.antigravity/` folder [4]. If you paste a hardcoded API key into the chat, the agent might encapsulate it into an auto-generated documentation artifact [2] and store it permanently in a KI, potentially surfacing that secret in future, unrelated workspaces.
6. _Mitigation:_ Never paste raw credentials into the chat. Always rely on `mcp_config.json` for external authentication [12, 13].
7. **Risk: Extraction Failure on Complex Tasks**
8. _Issue:_ If tasks are executed solely in "Fast" mode without generating Artifacts [1, 14], the automatic extraction engine has less structured data to build robust KIs.
9. _Mitigation:_ Use "Planning mode" for complex tasks to ensure rich artifacts (like Implementation Plans and Walkthroughs) are generated [9, 14], providing high-quality raw material for Knowledge Items.

Deliverables

**Enterprise Memory Governance Rule (****.agents/rules/knowledge-optimization.md****)** _Deploy this Workspace Rule to force the agent to produce high-quality artifacts specifically formatted for optimal Knowledge Item extraction._
    # Knowledge Item (KI) &amp; Artifact Optimization
    *Activation Mode: Always On*

    ## 1. Archival Preparation
    - When completing a complex task in Planning mode, your final Walkthrough artifact MUST include a section titled "Core Patterns".
    - This section should summarize the reusable code examples and architectural decisions made during the task to ensure the Antigravity KI extraction engine captures high-fidelity insights.

    ## 2. Memory Retrieval Mandate
    - Before generating an Implementation Plan for a new feature, explicitly search your available Knowledge Item summaries for similar past implementations.
    - If a relevant KI is found, study the embedded artifacts and reference the KI's title in your Implementation Plan to confirm historical alignment.

    ## 3. Secret Sanitization
    - NEVER include API keys, database URIs, or personal credentials in any generated artifact (Implementation Plan, Task List, or Walkthrough) to prevent sensitive data from being permanently extracted into global Knowledge Items.



Recommended Next Actions

1. **Audit Your Brain:** Press `Cmd + E` (Mac) or `Ctrl + E` (Windows) to open the Agent Manager, then press `Cmd + P` to open the quick picker [7, 15]. Type to search for existing Knowledge Items and open them in a split pane to review what the agent has learned about your coding style [3, 7].
2. **Force an Extraction:** Spin up an agent and instruct it to document your current workspace architecture into an artifact. Once the conversation concludes, observe how Antigravity extracts this into a persistent KI [2, 3].
3. **Review Sandbox Boundaries:** Remember that KIs are stored globally in `~/.antigravity/` [4]. If you are working in a highly restricted workspace, ensure your "Agent Non-Workspace File Access" settings are configured correctly to prevent the agent from pulling cross-project KIs if strict isolation is required [4, 16].

Verification Checklist

* [x] Defined Knowledge Items (KIs) as the persistent memory system consisting of summaries and artifact collections.
* [x] Contextualized KIs within the Key Artifacts ecosystem (Implementation Plans, Walkthroughs).
* [x] Detailed the automatic extraction and progressive retrieval mechanics.
* [x] Identified memory staleness and secret leakage as operational risks.
* [x] Provided a deployable Workspace Rule enforcing optimal artifact generation for KI extraction.

--------------------------------------------------------------------------------

Antigravity Key Artifacts: Task Management and Execution Architecture

Antigravity Mission Control online. Full platform context loaded. Planning-first sequence initiated…

Mission Brief

Within Google Antigravity’s Key Artifacts ecosystem, Task Lists and Task Groups function as the internal state-management and execution-tracking layer. While Implementation Plans predict the work and Walkthroughs summarize it, Task Lists and Task Groups break down complex operations into asynchronous, modular subtasks that allow the Agent to safely execute multiple actions in parallel without losing its trajectory.

Detailed Plan
    task_group:
      goal: "Deconstruct Task Lists and Task Groups within the Antigravity Key Artifacts architecture."
      execution_phases:
        - phase_1_orchestration:
            sub_agent: "Planner Agent"
            action: "Map the distinction between Task Lists (markdown artifacts) and Task Groups (UI-level breakdowns)."
        - phase_2_context_mapping:
            sub_agent: "Research Agent"
            action: "Analyze the anatomy of a Task Group, including overarching goals, file pills, and pending step resolution."
        - phase_3_risk_evaluation:
            sub_agent: "Critique &amp; Risk Agent"
            action: "Evaluate execution stalling during 'pending steps' requiring terminal or browser approvals."
        - phase_4_synthesis:
            sub_agent: "Coder/Builder Agent"
            action: "Generate a production-grade Workspace Rule enforcing strict task modularization and checklist maintenance."



Agent Execution Summary

* **Planner Agent track:** Confirmed the structural difference. A **Task List** is an actual artifact (a markdown checklist) the agent uses internally to monitor its progress across research, implementation, and verification phases [1]. A **Task Group** is the presentation layer used when the Agent is in Planning mode, breaking large problems down into smaller units of work [2].
* **Research Agent track:** Mapped the UI/UX interaction. Within a Task Group, subtask details are collapsed by default to reduce noise, but users can toggle them open to inspect the exact steps [3]. If an action requires human intervention (like terminal command approval), it surfaces in a special "pending steps" section at the end of the Task Group [3].
* **Critique Agent flag:** _Autonomy Bottleneck Detected._ Because Task Groups often execute multiple parts of a task at the same time [2], Strict Mode or "Request Review" policies will bottleneck the entire group if a subtask hits a terminal command or browser javascript execution that requires manual approval [3-6].

Deep Insights & Opportunities

Layer 1: Task Lists (The Internal Stateful Artifact)

To achieve true asynchronous orchestration, the agent cannot hold its entire execution state in its short-term memory window. Instead, it relies on the **Task List** artifact. Formatted as a live markdown list, this artifact tracks action items across research, implementation, and verification [1]. It provides a live snapshot of what the agent is currently doing [1]. Unlike Implementation Plans (where users leave heavy comments to alter scope), the official documentation notes that users typically do not need to interact directly with the Task List [1, 7]. It serves strictly as the agent’s internal compass to stay aligned with your overarching goal [1].

Layer 2: Task Groups (The Execution Orchestrator)

When the Agent operates in "Planning mode" on large and complex tasks, it deploys **Task Groups** [2, 8]. Task Groups are the framework that allows the agent to work on multiple parts of a greater task simultaneously [2]. The anatomy of a Task Group includes:

1. **Overarching Goal:** The top component specifies the main objective and summarizes the changes made in this unit of work [2].
2. **File Pills:** A section of edited files allows for quick user auditing; clicking a pill displays the current state of the changed file [2].
3. **Subtasks:** Modular progress updates that are hidden by default but expandable via a toggle if the user wants to audit the agent's exact steps [3].

Layer 3: Synergy within the Key Artifact Ecosystem

Task Lists and Task Groups bridge the gap between intent and completion. The lifecycle flows as follows: First, the Agent generates an **Implementation Plan** artifact for user review [9]. Once approved, the Agent shifts into execution, utilizing **Task Groups** to modularize the work and a **Task List** artifact to persistently track its state [1, 2]. Finally, upon finishing the Task Group, the Agent produces a **Walkthrough** artifact summarizing the changes [10]. This multi-layered approach frees the developer from synchronously monitoring the Agent step-by-step, unlocking true multi-agent parallelism [11].

Risks & Mitigations

1. **Risk: Silent Execution Halts (Pending Steps)**
2. _Issue:_ Inside Task Groups, subtasks might require terminal access or browser setup [3]. If your Terminal Command Auto Execution policy is set to "Request Review" (or Strict Mode is active), these actions generate "pending steps" at the end of the Task Group [3, 5, 6]. The agent will silently pause until you manually approve them.
3. _Mitigation:_ Regularly monitor the Inbox in the Agent Manager (`Cmd + E`), which centralizes notifications for any conversations awaiting your approval to run terminal commands or use the browser [12].
4. **Risk: Quota Drain via Over-Granular Planning**
5. _Issue:_ Because usage limits correlate with the "work done" (including hidden "Thinking Tokens" generated during internal deliberation) [13, 14], allowing the agent to generate massively bloated Task Groups for simple modifications can rapidly exhaust your 5-hour rolling quota [13, 15].
6. _Mitigation:_ Use "Fast mode" instead of "Planning mode" for simple, localized tasks (like renaming variables or running basic bash commands) to bypass the heavy Task Group and Artifact generation overhead [8].

Deliverables

**Enterprise Task Governance Rule (****.agents/rules/task-tracking.md****)** _Deploy this Workspace Rule to enforce disciplined Task List maintenance and prevent subtask bloat during complex Task Group execution._
    # Task List &amp; Task Group Governance
    *Activation Mode: Always On*

    ## 1. Task List Initialization
    - For any objective requiring more than 3 file modifications, immediately initialize a highly granular `Task List` artifact.
    - Structure the Task List into three strict phases: `[ ] Research`, `[ ] Implementation`, and `[ ] Verification`.

    ## 2. Task Group Subtask Constraints
    - Do not create more than 5 parallel subtasks within a single Task Group.
    - Ensure all terminal execution requests are batched to minimize "pending steps" that interrupt asynchronous workflows.

    ## 3. Quota Protection
    - If the user requests a simple variable rename or formatting fix, bypass Task Group generation and execute directly to conserve reasoning tokens.



Recommended Next Actions

1. **Inspect Active Subtasks:** In your current Agent Manager conversation, locate an active Task Group and toggle the expand button on a progress update to audit the exact micro-steps the agent is taking [3].
2. **Clear Pending Steps:** Review the bottom of your Task Groups for the "special section" containing pending terminal or browser approvals to unblock stalled agents [3].
3. **Toggle Fast Mode:** If you are executing simple tasks, navigate to the Agent Side Panel and switch from Planning Mode to Fast Mode to execute instantly without generating complex Task Group artifacts [8].

Verification Checklist

* [x] Differentiated Task Lists (artifacts) from Task Groups (planning structures).
* [x] Detailed the internal anatomy of Task Groups (goals, file pills, subtasks, pending steps).
* [x] Contextualized within the broader Key Artifacts lifecycle (Implementation Plans, Walkthroughs).
* [x] Addressed execution interruptions and Strict Mode / Review Policy bottlenecks.
* [x] Provided a copy-pasteable Workspace Rule to enforce tracking standards.

--------------------------------------------------------------------------------

The Antigravity Orchestration Architecture and Implementation Blueprint

Antigravity Mission Control online. Full platform context loaded. Planning-first sequence initiated…

Mission Brief

Within Google Antigravity’s asynchronous orchestration architecture, Implementation Plans serve as the foundational predictive artifact. In the larger ecosystem of Key Artifacts—which shifts development from synchronous babysitting to asynchronous review—the Implementation Plan acts as the primary human-in-the-loop architectural blueprint, pausing autonomous execution to ensure technical alignment before code is mutated.

Detailed Plan
    task_group:
      goal: "Deconstruct Implementation Plans and their operational mechanics within Antigravity's Key Artifacts ecosystem."
      execution_phases:
        - phase_1_orchestration:
            sub_agent: "Planner Agent"
            action: "Map the temporal artifact taxonomy: Predictive (Implementation Plans), Stateful (Task Lists), and Reflective (Walkthroughs)."
        - phase_2_context_mapping:
            sub_agent: "Research Agent"
            action: "Analyze the interactive feedback loop, specifically how developers use comments to alter scope, tech stacks, and logic."
        - phase_3_risk_evaluation:
            sub_agent: "Critique &amp; Risk Agent"
            action: "Evaluate execution stalling caused by the 'Artifact Review Policy' and 'Strict Mode' overrides."
        - phase_4_synthesis:
            sub_agent: "Coder/Builder Agent"
            action: "Generate a production-grade Workspace Rule to enforce rigorous Implementation Plan standards."



Agent Execution Summary

* **Planner Agent track:** Confirmed the temporal relationship of Key Artifacts. When operating in "Planning mode," the Agent produces Artifacts to asynchronously communicate with the user [1, 2]. Implementation Plans act as the pre-execution blueprint [3], Task Lists act as the real-time execution state [4], and Walkthroughs serve as the post-execution summary [5].
* **Research Agent track:** Mapped the human-in-the-loop interaction model. Users are not forced to accept an Implementation Plan outright. They can leave comments on the artifact to decrease scope or shift the tech stack, forcing the agent to iterate and re-request review before modifying source code [6, 7].
* **Critique Agent flag:** _Autonomy Bottleneck Detected._ The velocity of the Agent is entirely dependent on the "Artifact Review Policy" [8]. If Strict Mode is enabled, the system overrides all autonomy settings and forces a "Request Review" state for all artifacts, completely stalling the agent until a human clicks "Proceed" [9].

Deep Insights & Opportunities

Layer 1: The Architectural Blueprint (Predictive State)

In Antigravity, an Artifact is defined as any object the agent creates to accomplish its work or communicate its thinking (e.g., markdown files, diff views, diagrams, screenshots) [2]. The **Implementation Plan** is the most critical of these because it represents the _predictive_ state of the codebase. It contains the technical details of what revisions the Agent intends to make to accomplish a complex task [3]. Rather than instantly vomiting code into the editor, the Agent pauses, presents the Implementation Plan in the Agent Manager or Editor, and waits for strategic alignment [3, 10].

Layer 2: The Artifact Feedback Engine

Antigravity supports a rich, asynchronous feedback loop directly attached to the Implementation Plan. Often, an Agent will draft a plan that slightly misaligns with enterprise architecture [6]. Instead of canceling the task, developers can toggle the "Review" button in the artifact header and leave specific comments (e.g., "Use PostgreSQL instead of SQLite," or "Decrease the scope to just the frontend UI") [6]. The Agent consumes this feedback, iterates on the Implementation Plan, and either begins work or re-requests your review [7].

Layer 3: Contextualizing within the Artifact Ecosystem

To understand the Implementation Plan, you must view it within the full lifecycle of an Antigravity task:

1. **Preparation:** The Agent drafts the **Implementation Plan** to propose changes [3].
2. **Execution:** Once the user clicks "Proceed" [3, 6], the Agent tracks its live progress using a **Task List** (a markdown checklist of research, implementation, and verification steps that the user typically does not need to interact with) [4].
3. **Completion:** Upon finishing the task, the Agent generates a **Walkthrough** artifact, summarizing the changes made so the user can quickly get up to speed [5]. If UI changes were made, this Walkthrough often embeds **Browser Recordings** or **Screenshot** artifacts [5, 11, 12].
4. **Persistence:** The insights from these artifacts are then automatically extracted into **Knowledge Items (KIs)**, forming the agent's persistent memory for future conversations [13, 14].

Risks & Mitigations

1. **Risk: Strict Mode Execution Paralysis**
2. _Issue:_ If "Strict Mode" is enabled, Antigravity overrides your baseline autonomy settings and forces the Artifact Review policy to "Request Review" [9]. The Agent will completely halt at the Implementation Plan phase until manual human approval is provided.
3. _Mitigation:_ For trusted, highly constrained local workspaces, ensure Strict Mode is disabled and navigate to Settings -> Agent to explicitly toggle the Artifact Review Policy to "Always Proceed" [8, 15]. This allows the Agent to draft the plan and immediately execute it.
4. **Risk: Implementation Drift & Scope Creep**
5. _Issue:_ Developers suffering from review fatigue may instinctively click "Proceed" [3] on a massive Implementation Plan without verifying the architectural choices, leading to unwanted framework imports or destructive refactoring.
6. _Mitigation:_ Leverage custom Rules to bound the Agent's planning logic. Mandate that every Implementation Plan must include a "Rollback Strategy" or a "Scope Constraint" section before it is allowed to request human review.

Deliverables

**Enterprise Artifact Governance Rule (****.agents/rules/plan-validation.md****)** _Deploy this Workspace Rule to enforce rigorous Implementation Plan generation standards before the Agent requests your review._
    # Implementation Plan &amp; Artifact Standards
    *Activation Mode: Always On*

    ## 1. Predictive Blueprinting
    - NEVER bypass the Implementation Plan phase for tasks involving more than 2 file modifications.
    - Every Implementation Plan MUST include three distinct sections:
      1. **Proposed Architecture:** (What files are changing and why)
      2. **Tech Stack Constraints:** (Confirming alignment with workspace standards)
      3. **Rollback Strategy:** (How to revert if execution fails)

    ## 2. Artifact Ecosystem Integration
    - While executing the approved Implementation Plan, maintain a highly granular Task List artifact to track terminal and browser states.
    - Upon completion, generate a Walkthrough artifact summarizing the exact delta between the initial plan and the final committed code.



Recommended Next Actions

1. **Configure Artifact Autonomy:** Navigate to Settings -> Agent and locate the "Artifact Review Policy" [8]. Set it to "Always Proceed" for rapid prototyping environments, or keep it at "Request Review" for production-grade codebases [8, 15].
2. **Test the Feedback Loop:** Spawn an Agent and assign it a complex feature. When it generates the Implementation Plan, do not click Proceed. Instead, use the commenting feature to enforce a deliberate constraint (e.g., "Refine this plan to use only Tailwind utility classes"), and observe the iteration cycle [6, 7].
3. **Review the Inbox:** Open the Agent Manager (`Cmd + E` or `Ctrl + E`) [16] and check your Inbox view [17]. Pending Implementation Plans from parallel background agents will surface here, awaiting your approval to unblock execution [17].

Verification Checklist

* [x] Defined Implementation Plans as the predictive blueprinting artifact.
* [x] Contextualized the artifact within Task Lists, Walkthroughs, and KIs.
* [x] Detailed the commenting, iteration, and "Proceed" feedback loop.
* [x] Identified bottlenecks related to Artifact Review Policies and Strict Mode.
* [x] Provided a deployable Workspace Rule enforcing plan structures.

--------------------------------------------------------------------------------

The Google Antigravity Artifact Architecture and Multi-Agent Orchestration Guide

Antigravity Mission Control online. Full platform context loaded. Planning-first sequence initiated…

Mission Brief

Within Google Antigravity’s orchestration architecture, Artifacts serve as the primary asynchronous communication and state-management bridge between the autonomous reasoning models and the human developer [1]. I will now deconstruct the platform's key artifact types—Implementation Plans, Task Lists, Walkthroughs, and Visual Recordings—and detail how they interlock with Agent Review Policies and Persistent Knowledge to scale your multi-agent workflows.

Detailed Plan
    task_group:
      goal: "Deconstruct Key Artifacts and their operational mechanics within Antigravity's multi-agent architecture."
      execution_phases:
        - phase_1_orchestration:
            sub_agent: "Planner Agent"
            action: "Map the core artifact taxonomy: Implementation Plans, Task Lists, and Walkthroughs."
        - phase_2_context_mapping:
            sub_agent: "Browser/External Agent"
            action: "Analyze visual artifacts: Browser Recordings and Screenshots generated during UI automation."
        - phase_3_risk_evaluation:
            sub_agent: "Critique &amp; Risk Agent"
            action: "Evaluate execution stalling caused by Artifact Review Policies and Strict Mode enforcement."
        - phase_4_synthesis:
            sub_agent: "Coder/Builder Agent"
            action: "Generate a production-grade Workspace Rule enforcing strict artifact generation and review standards."



Agent Execution Summary

* **Planner Agent track:** Confirmed that Artifacts are explicitly produced when the Agent operates in "Planning mode" [2], [3]. They shift the developer experience from synchronously babysitting code generation to asynchronously reviewing rich markdown files, diff views, architecture diagrams, and task states [1].
* **Research Agent track:** Mapped the persistence layer. Artifacts are not entirely ephemeral; they are actively ingested into "Knowledge Items" (KIs)—Antigravity's persistent memory system—to inform future agent responses [4].
* **Critique Agent flag:** _Autonomy Bottleneck Detected._ The "Artifact Review Policy" dictates agent momentum. If set to "Request Review" (or if Strict Mode is active), the agent halts execution upon generating an Implementation Plan, requiring human feedback via comments before proceeding [5], [6], [7].

Deep Insights & Opportunities

Layer 1: The Core Artifact Taxonomy

Antigravity categorizes Artifacts based on their role in the execution trajectory:

* **Implementation Plans:** The architectural blueprint. Before modifying your codebase, the agent generates a technical plan detailing the necessary revisions [6]. Users can comment directly on this artifact to decrease scope, enforce a different tech stack, or correct discrepancies before clicking "Proceed" [8].
* **Task Lists:** The internal state tracker. Formatted as a markdown list, this artifact monitors progress across research, implementation, and verification phases [9]. It provides a live snapshot of the agent's internal logic, though it typically does not require direct human interaction [9].
* **Walkthroughs:** The post-execution summary. Generated upon task completion, Walkthrough artifacts provide a concise summary of codebase changes, allowing the developer to get up to speed asynchronously [10].
* **Visual Recordings & Screenshots:** When the Browser Subagent is actuated, it captures screenshots and screen recordings of its actions, saving them as visual artifacts for user review [11], [12]. Walkthroughs often embed these visual artifacts to demonstrate successful UI testing [10].

Layer 2: Asynchronous Multi-Agent Orchestration

Artifacts are the essential enablers of Antigravity's Agent Manager (Mission Control) [1], [3]. Because you can spin up multiple agents in parallel across different workspaces, it is physically impossible to watch every line of code being written [13]. Artifacts allow these parallel agents to pause, document their proposed state (Implementation Plan) or completed state (Walkthrough), and wait in the unified Inbox for your eventual review [3], [14].

Layer 3: Synergy with Knowledge Items (KIs)

Artifacts are the raw material for Antigravity's long-term memory. As agents create automatically generated documentation or code examples (which are types of artifacts), the system extracts this information into Knowledge Items [4]. When a relevant KI is recognized in a future conversation, the agent studies the embedded artifacts to maintain context across sessions [15].

Risks & Mitigations

1. **Risk: Strict Mode Execution Paralysis**
2. _Issue:_ Enabling Strict Mode forces the Artifact Review Policy to require manual approval, halting all autonomous agent progress until a human intervenes [7].
3. _Mitigation:_ For trusted, highly-constrained local workspaces, ensure Strict Mode is disabled and toggle the Artifact Review Policy to "Always Proceed" in the Agent Settings to achieve true zero-touch autonomy [5], [16].
4. **Risk: Implementation Drift**
5. _Issue:_ If the user proceeds with an Implementation Plan without verifying the details, the agent may execute massive, unwanted architectural changes.
6. _Mitigation:_ Utilize the Artifact commenting feature. Leave targeted feedback on the artifact; the agent will iterate on the plan and re-request review before touching the source code [8], [17].
7. **Risk: Unmonitored Browser Loops**
8. _Issue:_ The browser subagent may actuate continuously on background tabs [18], potentially failing silently if visual state validation isn't requested.
9. _Mitigation:_ Explicitly prompt the agent to take a screenshot of a page during execution to force the creation of a visual artifact, ensuring the UI state is correct [12].

Deliverables

**Enterprise Artifact Governance Rule (****.agents/rules/artifact-standards.md****)** _Deploy this Workspace Rule to enforce consistent artifact generation across complex multi-agent tasks._
    # Artifact Generation &amp; Review Standards
    *Activation Mode: Always On*

    ## 1. Implementation Plan Mandates
    - NEVER bypass the Implementation Plan phase for tasks involving more than 2 file modifications.
    - All Implementation Plans must include a "Rollback Strategy" section before requesting human review.

    ## 2. Walkthrough &amp; Visual Verification
    - Upon completing a task involving the Browser Subagent, you MUST generate a Walkthrough Artifact.
    - The Walkthrough MUST embed screenshot artifacts of the final DOM state or a browser recording artifact to prove successful execution.

    ## 3. Task List Maintenance
    - Maintain a highly granular Task List artifact for any task exceeding 5 steps. Update the Markdown checklist synchronously as you complete terminal commands.



Recommended Next Actions

1. **Configure Artifact Review Policies:** Navigate to Settings -> Agent and evaluate your "Artifact Review Policy". Switch to "Always Proceed" for rapid prototyping, or "Request Review" for production-grade codebases [5].
2. **Explore the Inbox:** Open the Agent Manager (`Cmd + E`) and check your Inbox to review pending Implementation Plans from background agents awaiting your approval [14].
3. **Audit Knowledge Items:** Check the Agent Manager for auto-generated Knowledge Items to see which of your past artifacts have been permanently committed to the agent's memory [4], [15].

Verification Checklist

* [x] Extracted all core Artifact types (Implementation Plans, Task Lists, Walkthroughs, Recordings) from the provided documentation.
* [x] Mapped the relationship between Artifacts, Planning Mode, and the Agent Manager.
* [x] Identified bottlenecks associated with Artifact Review Policies and Strict Mode.
* [x] Provided an actionable Workspace Rule to enforce artifact best practices.

--------------------------------------------------------------------------------

Antigravity Architecture: Mastering the Model Context Protocol Integration

Antigravity Mission Control online. Full platform context loaded. Planning-first sequence initiated…

Mission Brief

Within Google Antigravity’s Customization & Extensibility architecture, the Model Context Protocol (MCP) acts as the secure bridge connecting your local agents to the external world. While Rules, Workflows, and Skills manipulate local files and terminal commands, MCP integrates real-time context from external databases, SaaS tools, and cloud deployment pipelines directly into the agent's reasoning window.

Detailed Plan
    task_group:
      goal: "Deconstruct Antigravity's MCP Integration as the external capability layer of the extensibility architecture."
      execution_phases:
        - phase_1_orchestration:
            sub_agent: "Planner Agent"
            action: "Map the conceptual role of MCP: Context Resources (data fetching) vs. Custom Tools (action execution)."
        - phase_2_context_mapping:
            sub_agent: "Research Agent"
            action: "Analyze the configuration schema (mcp_config.json), supported transports (stdio, HTTP), and native authentication (Google ADC, OAuth)."
        - phase_3_risk_evaluation:
            sub_agent: "Critique &amp; Risk Agent"
            action: "Identify enterprise infrastructure limits, specifically missing mTLS properties and static secret binding."
        - phase_4_synthesis:
            sub_agent: "Coder/Builder Agent"
            action: "Generate a compliant mcp_config.json artifact demonstrating local tool and remote database integrations."



Agent Execution Summary

* **Planner Agent track:** Mapped the integration boundary. Instead of users manually pasting database schemas or build logs into the editor, MCP allows Antigravity to fetch this context directly or execute safe actions natively (like creating a Linear issue or searching Notion) [1, 2].
* **Research Agent track:** Decoded the `mcp_config.json` routing. Configured at `~/.gemini/antigravity/mcp_config.json` (or `C:\Users\

--------------------------------------------------------------------------------

Google Antigravity: Orchestrating Development with Agentic Workflows

Antigravity Mission Control online. Full platform context loaded. Planning-first sequence initiated…

Mission Brief

Within Google Antigravity’s Customization & Extensibility architecture, Workflows act as the active trajectory-level orchestration engine. While Rules provide persistent behavioral boundaries and Skills inject specialized capabilities, Workflows transform repetitive, multi-step procedures into sequential, slash-invokable (`/workflow-name`) Markdown files that autonomously guide agents through complex development cycles [1].

Detailed Plan
    task_group:
      goal: "Deconstruct Workflows (Slash Commands) as the sequential execution layer within Antigravity's extensibility triad."
      execution_phases:
        - phase_1_orchestration:
            sub_agent: "Planner Agent"
            action: "Map the conceptual and operational differences between Workflows, Rules, and Skills based on official documentation."
        - phase_2_context_mapping:
            sub_agent: "Research Agent"
            action: "Analyze Workflow creation methods (manual UI vs. Agent-generated) and file constraints (12,000 characters, Markdown format)."
        - phase_3_risk_evaluation:
            sub_agent: "Critique &amp; Risk Agent"
            action: "Evaluate execution interruptions caused by Strict Mode terminal sandboxing and context bloat via Workflow nesting."
        - phase_4_synthesis:
            sub_agent: "Coder/Builder Agent"
            action: "Generate a production-grade composable Workflow artifact demonstrating step-by-step logic and sub-agent handoffs."



Agent Execution Summary

* **Planner Agent track:** Mapped the core distinction. Rules provide persistent, reusable context (the _how_), while Workflows provide a structured sequence of interconnected steps (the _what_) [1].
* **Builder Agent track:** Verified the creation path. Workflows are configured via the `... -&gt; Customizations -&gt; Workflows` panel, can be scoped globally or to a specific workspace, and are limited to 12,000 characters per Markdown file [2, 3]. They are triggered by typing `/workflow-name` or `@workflows

--------------------------------------------------------------------------------

Antigravity Progressive Disclosure and Agent Skill Orchestration

Antigravity Mission Control online. Full platform context loaded. Planning-first sequence initiated…

Mission Brief

Within Google Antigravity’s Customization & Extensibility architecture, the "Progressive Disclosure" pattern is the foundational context-management engine that governs Agent Skills. I will now decompose how this three-phase orchestration mechanism (Discovery, Activation, Execution) securely injects capabilities on-demand, preventing context bloat and token quota exhaustion across your parallel workspaces.

Detailed Plan
    task_group:
      goal: "Deconstruct the Progressive Disclosure pattern and its role in optimizing YAML + Markdown Skills execution."
      execution_phases:
        - phase_1_orchestration:
            sub_agent: "Planner Agent"
            action: "Map the three mechanical phases of progressive disclosure against the Antigravity Skill architecture."
        - phase_2_context_mapping:
            sub_agent: "Research Agent"
            action: "Analyze the relationship between the YAML frontmatter and the Discovery phase."
        - phase_3_risk_evaluation:
            sub_agent: "Critique &amp; Risk Agent"
            action: "Evaluate semantic misrouting, monolithic skill anti-patterns, and script-parsing risks during Execution."
        - phase_4_synthesis:
            sub_agent: "Coder/Builder Agent"
            action: "Generate a targeted SKILL.md template optimized for the progressive disclosure lifecycle."



Agent Execution Summary

* **Planner Agent track:** Mapped the progressive disclosure lifecycle. Skills are not loaded entirely into the prompt at runtime. Instead, the agent traverses three phases: Discovery, Activation, and Execution [1].
* **Research Agent track:** Confirmed the semantic trigger mechanism. During the "Discovery" phase, the agent only reads the `name` and `description` fields located in the YAML frontmatter of the `SKILL.md` files [1, 2]. It does not read the Markdown body unless activated.
* **Critique Agent flag:** _Context Protection Vulnerability._ Because the agent relies entirely on the YAML description to decide whether to activate a skill, vague descriptions or "do everything" skills will bypass the benefits of progressive disclosure, flooding the context window with irrelevant Markdown during unrelated tasks [3].

Deep Insights & Opportunities

Layer 1: The Mechanics of Progressive Disclosure

While Global Rules (`GEMINI.md`) and Workspace Rules (`.agents/rules/`) can act as "Always On" constraints that continuously occupy the reasoning model's prompt [4], Skills operate as an on-demand toolbelt via progressive disclosure [1].

1. **Discovery:** When a conversation initiates, the agent performs a lightweight scan, seeing _only_ the names and descriptions of the skills available in `

--------------------------------------------------------------------------------

The Architecture of Antigravity Reusable Knowledge Packages

Antigravity Mission Control online. Full platform context loaded. Planning-first sequence initiated…

Mission Brief

Within Google Antigravity, Skills are explicitly defined as "reusable packages of knowledge that extend what the agent can do" [1]. By encapsulating YAML-based semantic routing, Markdown-based execution logic, and optional local scripts into a single modular folder, these packages securely inject specialized capabilities into the agent's context without bloating the baseline token quota [2], [1], [3].

Detailed Plan
    task_group:
      goal: "Deconstruct 'Reusable Knowledge Packages' within the Antigravity Skills architecture."
      execution_phases:
        - phase_1_orchestration:
            sub_agent: "Planner Agent"
            action: "Map the internal anatomy of a knowledge package: instructions, best practices, and optional scripts."
        - phase_2_context_mapping:
            sub_agent: "Research Agent"
            action: "Analyze the 'Progressive Disclosure' engine (Discovery, Activation, Execution) that governs these packages."
        - phase_3_risk_evaluation:
            sub_agent: "Critique &amp; Risk Agent"
            action: "Evaluate structural anti-patterns, including 'do-everything' monolithic skills and context-breaking script parsing."
        - phase_4_synthesis:
            sub_agent: "Coder/Builder Agent"
            action: "Generate a production-grade SKILL.md template demonstrating decision trees and black-box script handling."



Agent Execution Summary

* **Planner Agent track:** Mapped the physical structure. A reusable knowledge package is a folder containing a `SKILL.md` file [2], [3]. These folders reside in `

--------------------------------------------------------------------------------

Architecting Antigravity Agent Skills via Progressive Disclosure

Antigravity Mission Control online. Full platform context loaded. Planning-first sequence initiated…

Mission Brief

Within Google Antigravity’s Customization & Extensibility architecture, Skills represent the dynamic capability-injection layer. By combining YAML frontmatter for semantic routing with Markdown for execution instructions, Skills allow developers to safely bundle specialized logic, custom scripts, and external integrations without overwhelming the reasoning model’s context window.

Detailed Plan
    task_group:
      goal: "Deconstruct the YAML + Markdown architecture of Agent Skills and optimize capability injection via Progressive Disclosure."
      execution_phases:
        - phase_1_orchestration:
            sub_agent: "Planner Agent"
            action: "Map the file structures (.agents/skills vs ~/.gemini/antigravity/skills) and YAML frontmatter requirements."
        - phase_2_context_mapping:
            sub_agent: "Research Agent"
            action: "Analyze the 'Progressive Disclosure' engine (Discovery -&gt; Activation -&gt; Execution)."
        - phase_3_risk_evaluation:
            sub_agent: "Critique &amp; Risk Agent"
            action: "Identify semantic routing failures, legacy path deprecations, and script parsing inefficiencies."
        - phase_4_synthesis:
            sub_agent: "Coder/Builder Agent"
            action: "Generate a production-grade SKILL.md template incorporating black-box script execution and decision trees."



Agent Execution Summary

* **Planner Agent track:** Mapped the physical architecture. A Skill is not a single file, but a folder containing a `SKILL.md` file [1]. Workspace skills live in `

--------------------------------------------------------------------------------

Antigravity Rule Activation and Context Management Architecture

Antigravity Mission Control online. Full platform context loaded. Planning-first sequence initiated…

Mission Brief

Within Google Antigravity’s Customization & Extensibility architecture, Rule Activation Modes (Always On, Manual, Model Decision, Glob) serve as the intelligent context-routing engine. I will now decompose how these four activation triggers prevent context window bloat, protect your token quotas, and ensure your Markdown rules are injected with surgical precision.

Detailed Plan
    task_group:
      goal: "Deconstruct Rule Activation Modes and their impact on context management and token quota within Antigravity."
      execution_phases:
        - phase_1_orchestration:
            sub_agent: "Planner Agent"
            action: "Define the four distinct activation triggers (Manual, Always On, Model Decision, Glob) and their operational scopes."
        - phase_2_context_mapping:
            sub_agent: "Research Agent"
            action: "Cross-reference activation modes with the 12,000-character rule limits and the Customizations UI."
        - phase_3_risk_evaluation:
            sub_agent: "Critique &amp; Risk Agent"
            action: "Analyze the relationship between 'Always On' activation, hidden Thinking Tokens, and 5-hour rolling Vertex AI quotas."
        - phase_4_synthesis:
            sub_agent: "Coder/Builder Agent"
            action: "Generate an optimized workspace rule architecture utilizing specific Glob and Model Decision triggers."



Agent Execution Summary

* **Planner Agent track:** Mapped the activation triggers. Rules can be configured with advanced activation options: Always On, Manual @mention, Model Decision, and Glob patterns [1, 2]. These determine exactly when the agent loads a rule's constraints into its prompt.
* **Research Agent track:** Verified the application layer. These triggers can be set for both Global rules (`~/.gemini/GEMINI.md`) and Workspace rules (`.agents/rules/`) via the Customizations panel in the Agent side panel [2, 3]. Every rule is capped at 12,000 characters [2].
* **Critique Agent flag:** _Critical Token Quota Risk._ Antigravity bills usage based on "work done," including hidden "Thinking Tokens" generated during the agent's internal deliberation process [4]. If a massive rule is set to "Always On," it inflates the baseline prompt for _every_ task, rapidly exhausting the 5-hour quota for Pro/Ultra users [4, 5].

Deep Insights & Opportunities

Layer 1: The Context Routing Engine (The Four Modes)

Antigravity Rules are persistent Markdown instructions that guide the agent's behavior, but they are only useful if they don't drown out the user's immediate prompt [1]. To manage this, Antigravity uses four distinct activation mechanisms defined at the rule level:

1. **Always On:** The rule is applied universally to every agent interaction [2]. This should be strictly reserved for absolute boundaries (e.g., "Never auto-execute network commands").
2. **Manual:** The rule is completely dormant until explicitly activated via an `@mention` in the Agent's input box [2]. This is ideal for niche workflows or one-off formatting standards.
3. **Model Decision:** The agent dynamically evaluates a natural language description of the rule to decide if it should apply it to the current task [2]. This introduces heuristic, semantic-based rule injection.
4. **Glob:** The rule is conditionally applied based on file path patterns (e.g., `*.js`, `src/**/*.ts`) [2]. The rule will only be injected into the context when the agent modifies files matching the pattern [2].

Layer 2: Surgical Precision via Glob and `@filename`

The integration of Glob patterns is the most powerful extensibility hook for enterprise environments. Because Workspace rules allow multiple Markdown files, developers can partition their logic [6]. You can have a `react-rules.md` activated purely by `*.tsx`, and a `python-rules.md` activated by `*.py`. Furthermore, within these conditionally activated rules, you can use the `@filename` syntax to pull in secondary documents [7]. If `@/docs/api.md` is referenced inside a Glob-activated rule, it will resolve as an absolute path or relative to the workspace, seamlessly bridging external knowledge without permanent context bloat [7].

Layer 3: Strategic Edge Cases & Model Orchestration

When orchestrating multiple parallel agents across workspaces—a core feature managed via the Agent Manager—activation triggers prevent "context collision" [8-10]. If you spawn five agents simultaneously, an "Always On" rule forces all five reasoning models to parse those constraints on every cycle [2, 9]. By delegating to "Model Decision" or "Glob," the Agent Manager can optimize the payload for the specific sub-agents (like the Browser Subagent or Terminal Subagent) automatically dispatched to handle the work [8, 9, 11].

Risks & Mitigations

1. **Risk: Vertex AI Quota Exhaustion**
2. _Issue:_ Agent limits correlate with "work done" and hidden "Thinking Tokens" [4]. A 12,000-character "Always On" rule [2] attached to complex reasoning loops will quickly drain the 5-hour refresh quota on Pro/Ultra plans [5].
3. _Mitigation:_ Audit your Customizations panel [3]. Limit "Always On" rules to < 1,000 characters. Shift all language, styling, and framework-specific constraints to "Glob" activation [2].
4. **Risk: Legacy Path Resolution Failures**
5. _Issue:_ Rules heavily relying on `@filename` includes may break if the directory structure changes, causing the agent to hallucinate missing context. Relative paths resolve relative to the rules file, while absolute paths fall back to the repository root if not found locally [7].
6. _Mitigation:_ Use strict workspace-relative pathing (e.g., `@/architecture/state.md`) within your `.agents/rules/` files to ensure consistent resolution regardless of where the rule activates [2, 7].
7. **Risk: Semantic Overlap in Model Decision**
8. _Issue:_ If multiple rules use "Model Decision" with vague natural language descriptions [2], the reasoning model may incorrectly activate conflicting rules.
9. _Mitigation:_ Make Model Decision descriptions mutually exclusive (e.g., "Use ONLY for database migration tasks" vs. "Use ONLY for frontend UI tasks").

Deliverables

**Enterprise Activation Optimization Guide (For manual or UI configuration)** _To apply these triggers, open the Editor, click_ _... -&gt; Customizations -&gt; Rules_ _and configure the activation dropdowns per file [3]._
    ### 1. Global Safety Rule (`~/.gemini/GEMINI.md`)
    **Activation Mode:** Always On
    **Purpose:** Universal guardrails that must never be bypassed.
    **Content Example:**
    "Never auto-execute destructive shell commands (e.g., rm -rf). Always pause for human review. Strict adherence to Google Antigravity Strict Mode restrictions."

    ### 2. Framework Rule (`.agents/rules/frontend.md`)
    **Activation Mode:** Glob
    **Glob Pattern:** `src/components/**/*.tsx`, `*.css`
    **Purpose:** surgical injection of React/Tailwind styling conventions only when relevant files are touched.

    ### 3. Architecture Rule (`.agents/rules/database.md`)
    **Activation Mode:** Model Decision
    **Description for Model:** "Apply this rule whenever the task involves modifying SQL schemas, Prisma clients, or database migrations."
    **Purpose:** Semantic triggering for cross-file conceptual tasks that cannot be captured by a simple Glob pattern.

    ### 4. Review Rule (`.agents/rules/pr-checklist.md`)
    **Activation Mode:** Manual
    **Purpose:** Triggered only when the user types `@pr-checklist` in the chat to audit code before committing via the Source Control tab.



Recommended Next Actions

1. **Refactor the Customizations Panel:** Open `... -&gt; Customizations -&gt; Rules` [3] and immediately demote any framework-specific rules from "Always On" to "Glob" [2].
2. **Leverage Multi-Agent Testing:** Open the Agent Manager (`Cmd + E`), spawn two parallel agents [10, 12], and instruct one to edit a `.js` file and another a `.py` file to verify that your Glob activation patterns isolate the constraints successfully [2].
3. **Check Legacy Rule Folders:** Ensure your rules reside in the updated `.agents/rules` folder rather than the deprecated `.agent/rules` directory, though backward compatibility is maintained [7].

Verification Checklist

* [x] Defined all four Activation Modes (Always On, Manual, Model Decision, Glob) [2].
* [x] Contextualized activation within the broader Customization & Rules framework (Global vs. Workspace) [2, 3].
* [x] Correlated "Always On" bloat with hidden Thinking Tokens and platform quota limits [4, 5].
* [x] Provided actionable mitigation strategies and configuration examples.

--------------------------------------------------------------------------------

Governing the Codebase: Google Antigravity Workspace Rules Architecture

Antigravity Mission Control online. Full platform context loaded. Planning-first sequence initiated…

Mission Brief

Within Google Antigravity’s Customization & Extensibility architecture, Workspace Rules (`.agents/rules/`) function as the project-scoped governance plane. Unlike Global Rules that universally affect every agent, Workspace Rules enforce isolated, repository-specific constraints—such as framework conventions, directory structures, and localized security boundaries—without polluting the context window of unrelated projects [1, 2].

Detailed Plan
    task_group:
      goal: "Deconstruct Workspace Rules (.agents/rules/) and their operational mechanics within Antigravity's extensibility model."
      execution_phases:
        - phase_1_orchestration:
            sub_agent: "Planner Agent"
            action: "Map the file architecture of Workspace Rules and UI invocation paths."
        - phase_2_context_mapping:
            sub_agent: "Research Agent"
            action: "Analyze rule activation triggers, multi-file support, and @filename inclusion logic."
        - phase_3_risk_evaluation:
            sub_agent: "Critique &amp; Risk Agent"
            action: "Identify structural risks, including legacy directory deprecations and path resolution fallbacks."
        - phase_4_synthesis:
            sub_agent: "Coder/Builder Agent"
            action: "Generate a scalable, production-ready Workspace Rule artifact."



Agent Execution Summary

* **Planner Agent track:** Verified project-level isolation. Workspace Rules are generated via the `... -&gt; Customizations -&gt; Rules -&gt; + Workspace` panel and saved directly into the `.agents/rules/` directory at the workspace or git root [2, 3].
* **Research Agent track:** Confirmed modularity. Unlike a monolithic `GEMINI.md`, the `.agents/rules/` directory supports multiple distinct Markdown files [1]. Each file is strictly capped at 12,000 characters [2].
* **Critique Agent flag:** _Path Resolution Edge Case Detected._ When using `@filename` mentions inside a Workspace Rule, relative paths resolve relative to the rule's location, while absolute paths (if not found locally) fallback to resolving relative to the repository root [4].

Deep Insights & Opportunities

Layer 1: Localized Governance vs. Global Overreach

While Global Rules (`~/.gemini/GEMINI.md`) establish your baseline developer identity, Workspace Rules (`.agents/rules/`) establish the physical reality of the codebase. By supporting multiple `.md` files in this directory [1], Antigravity allows you to modularize your constraints. You can have one file for backend API standards and another exclusively for frontend styling, providing persistent, reusable context at the prompt level [5].

Layer 2: Precision Activation via Glob Routing

To prevent context window exhaustion—which rapidly burns through your Vertex AI token limits via hidden "Thinking Tokens" [6]—Workspace Rules heavily leverage conditional activation. Instead of applying all rules "Always On", you can configure them to trigger via:

1. **Manual:** Activated strictly via `@mention` in the prompt [2].
2. **Model Decision:** The agent infers relevance based on your natural language description [2].
3. **Glob Pattern:** The most powerful extensibility hook. By setting a pattern like `*.js` or `src/**/*.ts`, the rule is only injected into the context window when the agent is actively editing those specific files [2].

Layer 3: Interlocking with Workflows and Skills

Workspace Rules serve as the passive foundation for active execution. While Rules provide persistent prompt-level guidance, Workflows (invoked via `/workflow-name`) provide trajectory-level sequential steps [5]. Simultaneously, Skills (`.agents/skills/`) inject progressive, on-demand capabilities via YAML frontmatter and external scripts [7, 8]. A properly architected workspace uses Rules to say _how_ to code, Workflows to say _what steps_ to take, and Skills to provide the _tools_ to do it.

Risks & Mitigations

1. **Risk: Legacy Path Compatibility Breakage**
2. _Issue:_ Older Antigravity projects may use the deprecated `.agent/rules/` directory (singular "agent").
3. _Mitigation:_ While Antigravity maintains backward compatibility for `.agent/rules/`, the system now defaults to `.agents/rules/` (plural) [4]. Rename legacy folders to ensure forward compatibility with future platform updates.
4. **Risk:** **@filename** **Context Failures**
5. _Issue:_ Referencing supplementary documentation via `@/docs/api.md` might fail if the pathing logic is misunderstood.
6. _Mitigation:_ Remember the strict Antigravity resolution cascade: A relative path resolves relative to the Rules file [4]. An absolute path (e.g., `@/path/to/file.md`) first attempts a true absolute OS resolution, and if it fails, resolves relative to the workspace root (`workspace/path/to/file.md`) [4].
7. **Risk: "Always On" Quota Drain per Workspace**
8. _Issue:_ Creating massive, multi-file rules set to "Always On" will consume the 5-hour rolling token quota (for Pro/Ultra users) on every single task [6, 9].
9. _Mitigation:_ Strictly enforce Glob patterns for language-specific Workspace Rules [2].

Deliverables

**Enterprise-Grade Workspace Rule Component (****.agents/rules/frontend-standards.md****)** _Deploys conditionally only when interacting with frontend components._
    # Frontend React &amp; Tailwind Standards
    *Activation Mode: Glob (src/components/**/*.tsx)*

    ## 1. Architectural Boundaries
    - Enforce strict typing. No `any` types permitted in this workspace.
    - When modifying state logic, refer to the overarching architecture at `@/docs/state-management.md`.

    ## 2. Style &amp; Linting
    - All styling must be executed via Tailwind CSS utility classes.
    - Do not bypass the Antigravity artifact review policy. Generate an Implementation Plan Artifact for any component refactor exceeding 50 lines.

    ## 3. Sandboxing &amp; External Execution
    - Do not attempt to run `npm install` for unauthorized packages. If a new dependency is required, pause execution and request human review.



Recommended Next Actions

1. **Audit Workspace Directories:** Open your current repository and ensure any legacy `.agent/rules` folders are renamed to `.agents/rules` [4].
2. **Modularize by Glob:** Open the UI (`... -&gt; Customizations -&gt; Rules -&gt; Workspace tab`) [3]. Break apart any single rule exceeding 12,000 characters [2] into multiple files bound to specific Glob patterns (e.g., `*.py`, `*.tsx`).
3. **Cross-Link Documentation:** Utilize the `@filename` mention capability [4] within your Workspace Rules to dynamically pull in existing project documentation (like a `CONTRIBUTING.md`), saving you from manually rewriting constraints.

Verification Checklist

* [x] Defined Workspace Rules (`.agents/rules/`) vs Global Rules.
* [x] Detailed the multi-file architecture and 12,000 character limits.
* [x] Explained Activation Modes (Glob, Model Decision) and `@filename` path resolution.
* [x] Addressed legacy directory backward compatibility (`.agent/rules`).
* [x] Provided a copy-pasteable Workspace Rule artifact.

--------------------------------------------------------------------------------

Antigravity Mission Control: Global Governance and Extensibility Framework

Antigravity Mission Control online. Full platform context loaded. Planning-first sequence initiated…

Mission Brief

Within Google Antigravity’s Customization & Extensibility architecture, Global Rules (`GEMINI.md` and `AGENTS.md`) serve as the universal, host-level governance plane. Unlike workspace-scoped rules, these passive Markdown constraints inject baseline behavioral, safety, and stylistic boundaries across every active agent and project simultaneously, acting as the ultimate root authority for multi-agent orchestration.

Detailed Plan
    task_group:
      goal: "Deconstruct the role, mechanisms, and risks of Global Rules (GEMINI.md) within Antigravity's extensibility framework."
      execution_phases:
        - phase_1_orchestration:
            sub_agent: "Planner Agent"
            action: "Map the host-level directory structure (~/.gemini/GEMINI.md) and UI invocation paths for Global Rules."
        - phase_2_context_mapping:
            sub_agent: "Research Agent"
            action: "Analyze the operational differences between Global Rules, Workspace Rules, and cross-tool compatibility (AGENTS.md)."
        - phase_3_risk_evaluation:
            sub_agent: "Critique &amp; Risk Agent"
            action: "Evaluate token exhaustion via 'Always On' activation, cross-workspace contamination, and secret exposure."
        - phase_4_synthesis:
            sub_agent: "Coder/Builder Agent"
            action: "Generate a production-grade GEMINI.md template utilizing Glob activation and universal security constraints."



Agent Execution Summary

* **Planner Agent track:** Verified the host-level architecture. Global Rules live in `~/.gemini/GEMINI.md` and apply to every workspace [1, 2]. They are capped at 12,000 characters [1, 2] and can be created manually or via the UI (`... -&gt; Customizations -&gt; Rules -&gt; + Global`) [3].
* **Research Agent track:** Confirmed standard compatibility. Antigravity explicitly supports `~/.gemini/AGENTS.md` as a global format, enabling direct rule parity for teams migrating from Cursor or using Claude Code [1, 4].
* **Critique Agent flag:** _Critical Token Quota Risk Detected._ Global Rules apply universally. If set to "Always On," a 12,000-character `GEMINI.md` file will inject massive context into _every_ prompt. Because Antigravity counts internal "Thinking Tokens" against your 5-hour rolling limit (Pro/Ultra plans), a bloated Global Rule will rapidly exhaust your quota before the agent even touches project code [2, 5].

Deep Insights & Opportunities

Layer 1: The Universal Governance Plane

In Antigravity's Markdown-driven extensibility model, Global Rules establish the baseline operating system for your agents. While Workspace Rules (`.agents/rules/`) dictate _project-specific_ tech stacks, Global Rules (`~/.gemini/GEMINI.md`) dictate the _developer's_ universal standards [1, 2]. This is where you enforce overarching behaviors: universal Git commit formats, strict TypeScript-first mandates, and definitive "Never do X" security constraints that must survive across parallel agent sessions [1].

Layer 2: Advanced Activation & Glob Routing

To mitigate the context bloat of injecting Global Rules into every reasoning cycle, Antigravity provides advanced activation engines. Instead of "Always On", Global Rules can trigger via:

1. **Manual:** Only when `@mentioned` in the chat [1, 2].
2. **Model Decision:** The agent infers relevance based on your natural language description [2].
3. **Glob Pattern:** Triggering only on specific file types (e.g., `*.js`, `src/**/*.ts`) [1, 2]. This creates a powerful paradigm where a single `GEMINI.md` file acts as a dynamic rule router, conditionally loading constraints only when the terminal or specific file extensions are active [2].

Layer 3: The Cross-Tool Migration Vector

Antigravity's support for `AGENTS.md` represents a massive strategic opportunity for enterprise deployment. Instead of rewriting rules, developers can copy their legacy `.cursorrules` directly into the `~/.gemini/AGENTS.md` file [1, 6]. This provides immediate, out-of-the-box governance continuity when transitioning local development workflows to Antigravity's multi-agent architecture [6].

Risks & Mitigations

1. **Risk: Global Quota Exhaustion (The "Always On" Trap)**
2. _Issue:_ Antigravity bills "work done" via hidden Thinking Tokens. A massive Global Rule applied "Always On" to parallel agents will rapidly deplete the 5-hour Vertex AI limit [5, 7].
3. _Mitigation:_ Use Glob patterns (`*.py`, `*.tsx`) in your Global Rules so the model only processes those constraints when explicitly modifying relevant files [2].
4. **Risk: Secret Leakage to the Agent Context**
5. _Issue:_ Because Global Rules reside in the user's root `~/.gemini/` directory, there is a risk of users pointing to local credential files using `@filename` includes, which could leak into the prompt [8-10].
6. _Mitigation:_ Never hardcode API keys or absolute paths to local credential vaults inside `GEMINI.md`. Use the Model Context Protocol (MCP) `mcp_config.json` for secure data access [11, 12].
7. **Risk: Workspace Override Collisions**
8. _Issue:_ A Global Rule mandating "Always use React" will conflict with a Workspace Rule in an Angular project, causing agent planning loops.
9. _Mitigation:_ Keep `GEMINI.md` strictly limited to language-agnostic workflows (e.g., security, terminal execution bounds, communication style). Relegate framework rules to `.agents/rules/` [2].

Deliverables

**Enterprise Baseline Global Rule (****~/.gemini/GEMINI.md****)** _Deploy this to establish safe, quota-friendly global boundaries._
    # Antigravity Mission Control: Universal Baseline Directives
    *Activation Mode: Model Decision &amp; Glob (*.*)*

    ## 1. Core Operating Principles
    - You are operating within Google Antigravity.
    - Prioritize the "Planning" mode for complex architectural changes before execution.
    - If a task involves more than 3 files, automatically generate an implementation plan and request user review via `progress.md`.

    ## 2. Security &amp; Terminal Execution (Strict Mode Fallback)
    - NEVER auto-execute destructive terminal commands (`rm -rf`, `drop table`, `kubectl delete`). Always pause for human review.
    - If network access fails, assume Seatbelt (macOS) or nsjail (Linux) strict sandboxing is active and inform the user.

    ## 3. Quota Management
    - Write clean, cyclomatic-complexity &lt; 10 code.
    - Avoid circular reasoning in `task_plan.md` to conserve Vertex AI token limits.



Recommended Next Actions

1. **Migrate Legacy Context:** If you are migrating from Cursor, immediately move your global `.cursorrules` to `~/.gemini/AGENTS.md` to instantiate your base constraints [6].
2. **Audit Global vs. Workspace Scope:** Open the Customizations UI (`... -&gt; Customizations -&gt; Rules`) and verify that stack-specific instructions are moved to the "Workspace" tab, leaving only universal standards in the "Global" tab [3].
3. **Optimize Activation Toggles:** Edit your Global Rules and switch any 2,000+ character blocks from "Always On" to "Glob" or "Model Decision" to dramatically reduce background token consumption [2, 5].

Verification Checklist

* [x] Defined `GEMINI.md` within the macro Customization & Extensibility context.
* [x] Detailed Global vs Workspace architectural differences.
* [x] Highlighted the token limit scaling risks associated with Global rules.
* [x] Provided a ready-to-deploy Global Rule artifact.

--------------------------------------------------------------------------------

Architecting Governance: The Antigravity Customization and Extensibility Framework

Antigravity Mission Control online. Full platform context loaded. Planning-first sequence initiated…

Mission Brief

Google Antigravity’s Customization & Extensibility architecture is built on a streamlined, Markdown-first foundation, where Rules act as the persistent governance layer. I will now decode how Rules interlock with Workflows and Skills, highlight structural limitations in this paradigm, and provide production-ready artifacts to optimize your agentic workspace.

Detailed Plan
    task_group:
      goal: "Deconstruct Antigravity Rules (Markdown) within the broader Customization &amp; Extensibility architecture."
      execution_phases:
        - phase_1_orchestration:
            sub_agent: "Planner Agent"
            action: "Map the extensibility triad: Rules (persistent constraints), Workflows (sequential actions), and Skills (progressive capability injection)."
        - phase_2_context_mapping:
            sub_agent: "Research Agent"
            action: "Analyze Rule activation triggers, file locations, and compatibility layers (e.g., Cursor migration)."
        - phase_3_risk_evaluation:
            sub_agent: "Critique &amp; Risk Agent"
            action: "Evaluate host-based execution risks, token quota impacts, and missing strict schema constraints."
        - phase_4_synthesis:
            sub_agent: "Coder/Builder Agent"
            action: "Generate a compliant Workspace Rule artifact utilizing advanced @mentions and Glob targeting."



Agent Execution Summary

* **Planner Agent track:** Mapped the core hierarchy. Rules are passive, persistent constraints injected into the agent's prompt [1]. They work alongside Workflows (slash-invokable step-by-step guides) [1, 2] and Skills (YAML-frontmattered packages injected via progressive disclosure) [3, 4].
* **Research Agent track:** Verified exact file paths. Global rules live in `~/.gemini/GEMINI.md` or `~/.gemini/AGENTS.md`, while workspace rules reside in `.agents/rules/` [1, 5]. This establishes a 100% functional equivalent to Cursor's `.cursorrules` [1, 6].
* **Critique Agent flag:** _Architectural limitation detected._ Extensibility relies purely on natural language (Markdown) and basic YAML; there are no advanced JSON schemas, strict parameter typing, or native project-level Docker/gVisor containers to enforce execution boundaries [7].

Deep Insights & Opportunities

Layer 1: The Core Extensibility Triad

Antigravity avoids heavy extension APIs, favoring a text-based, human-readable extensibility model composed of three surfaces:

* **Rules (Passive Constraints):** Markdown files (capped at 12,000 characters) that enforce style, tech stacks, and safety bounds [1, 5]. They dictate _how_ the agent behaves globally or per-workspace [8].
* **Workflows (Sequential Execution):** Action-oriented Markdown files providing trajectory-level guidance for repetitive tasks, invoked via `/workflow-name` [2].
* **Skills (Progressive Disclosure):** Isolated capability folders containing a `SKILL.md` (with YAML frontmatter) that the agent auto-discovers and reads only when contextually relevant [3, 4].

Layer 2: Rule Activation & Context Routing

Unlike static prompt injection, Antigravity Rules feature a highly dynamic activation engine [5, 9]. You can control precisely when a rule consumes the reasoning model's context window:

1. **Always On:** Injected into every prompt [5].
2. **Manual:** Triggered strictly via `@mention` in the chat [5].
3. **Model Decision:** The agent evaluates a natural language description to decide if the rule applies [5].
4. **Glob Pattern:** Automatically triggered when editing specific files (e.g., `*.ts`, `src/**/*`) [5, 9].

Additionally, Rules support `@filename` references [10]. If you provide an absolute path, it resolves directly; if relative, it resolves relative to the Rule's location, allowing you to build modular, composable rule trees [10].

Layer 3: Strategic Edge Cases & Scaling Risks

Because Antigravity lacks native project-level containerization (like devcontainers), terminal commands run directly on the host [7, 11]. This elevates Rules from mere "coding guidelines" to critical governance boundaries. If an Agent is operating autonomously, it generates hidden "Thinking Tokens" which consume your baseline Vertex AI rate limits rapidly [12]. Overloading the agent with 12,000-character "Always On" rules will accelerate quota exhaustion [5, 12].

Risks & Mitigations

1. **Risk: Sandbox Deprecation & Host Exposure**
2. _Issue:_ Because there is no native Docker/gVisor sandboxing [7], macOS relies on Seatbelt (`sandbox-exec`), which is a deprecated legacy API [11].
3. _Mitigation:_ Use Rules in combination with Antigravity's **Strict Mode**, which automatically enforces network-denied sandboxing and requires explicit URL Allowlist/Denylist verification [13, 14].
4. **Risk: Token Exhaustion via Rule Bloat**
5. _Issue:_ Applying massive Rules universally drains the 5-hour rolling token quota (for Pro/Ultra users) due to excess "Thinking Tokens" during the planning phase [12, 15].
6. _Mitigation:_ Never use "Always On" for stack-specific rules. Utilize **Glob patterns** (e.g., `*.js`) so constraints only load when relevant files are active [5].
7. **Risk: Secrets Leakage via Global Access**
8. _Issue:_ Enabling "Agent Non-Workspace File Access" can expose local secrets to the agent's context window [16, 17].
9. _Mitigation:_ Keep sensitive logic in `.agents/rules/` (workspace-scoped) [5], and restrict Global rules (`~/.gemini/GEMINI.md`) to generic safety and style parameters.

Deliverables

**Enterprise-Hardened Workspace Rule (****.agents/rules/react-security.md****)** _Ready to deploy via_ _... -&gt; Customizations -&gt; Rules__._
    # React Security &amp; State Constraints
    *Activation Mode: Glob (*.jsx, *.tsx)*

    ## ───── Boundary Constraints ─────
    1. **Never** execute network-reaching terminal commands without explicit user approval.
    2. If `task_plan.md` modifications span multiple directories, reference @/docs/architecture.md before writing code.
    3. Use strict type checking. No `any` types allowed.

    ## ───── Telemetry &amp; External Actions ─────
    If external context is needed, utilize the connected Model Context Protocol (MCP) servers rather than raw curl commands.



Recommended Next Actions

1. **Migrate Legacy Rules:** If migrating from Cursor, directly copy your `.cursorrules` content into `~/.gemini/AGENTS.md` (for global use) or `.agents/rules/` (for workspace use) to instantly restore your custom governance [1].
2. **Decompose Monolithic Rules:** Audit your custom rules. If any rule file approaches the 12,000-character limit [5], break it apart and use `@filename` includes to nest context dynamically [10].
3. **Implement Strict Mode Controls:** Configure your settings to require "Request Review" for Terminal Auto Execution to prevent unverified script execution by the agent [18].

Verification Checklist

* [x] Defined Rules (Markdown) in relation to Skills and Workflows.
* [x] Documented activation methods and UI integration.
* [x] Cross-referenced security risks (Seatbelt deprecation, token limits).
* [x] Provided a grounded, copy-pasteable configuration artifact.

--------------------------------------------------------------------------------

Google Antigravity: Architecting Agentic Extensibility and Governance Boundaries

Antigravity Mission Control online. Full platform context loaded. Planning-first sequence initiated…

Mission Brief

Google Antigravity’s Customization and Extensibility architecture utilizes a deeply integrated triad of Rules, Workflows, and Skills written in Markdown and YAML, augmented by standard Model Context Protocol (MCP) integrations for external tool ingestion [1-3]. I will now decompose the platform's extensibility layers, highlight critical scaling risks, and provide actionable deliverables to harden your agentic environments.

Detailed Plan
    task_group:
      goal: "Synthesize Antigravity Customization &amp; Extensibility architecture, identify edge cases, and generate reusable artifacts."
      execution_phases:
        - phase_1_orchestration:
            sub_agent: "Planner Agent"
            action: "Map the foundational triad: Rules (persistent constraints), Workflows (sequential steps), and Skills (on-demand capability injection)."
        - phase_2_external_context:
            sub_agent: "Browser/External Agent"
            action: "Define MCP boundaries, context routing, and authentication mechanisms."
        - phase_3_risk_evaluation:
            sub_agent: "Critique &amp; Risk Agent"
            action: "Cross-reference documented system defects (Windows hook failures, semantic rule overlap, mTLS/secret rotation limits)."
        - phase_4_synthesis:
            sub_agent: "Coder/Builder Agent"
            action: "Generate production-grade Rule and Skill templates resolving known drift and pathing vulnerabilities."



Agent Execution Summary

* **Planner Agent track:** Confirmed that Antigravity relies entirely on host-based `.md` and `.yaml` configurations rather than project-level containerization (e.g., Docker/gVisor) [4, 5]. Verified that global rules reside in `~/.gemini/GEMINI.md` or `AGENTS.md`, and workspace rules in `.agents/rules/` [6, 7].
* **Builder Agent track:** Mapped the MCP schema. The platform natively uses `mcp_config.json` for extending context with databases (Neon, BigQuery) and tools (GitHub, Linear), handling OAuth and Google ADC natively [8-10].
* **Critique Agent flag:** _Critical vulnerability detected._ Workflow lifecycle hooks (`.agents/hooks/*.sh`) rely exclusively on Bash, causing silent and complete bypass of governance and commit-validation gates on Windows hosts without WSL2 workarounds [11].

Deep Insights & Opportunities

Layer 1: The Core Extensibility Surfaces

Antigravity's extensibility avoids heavy extension APIs in favor of natural language and simple markup:

* **Rules (Passive Constraints):** Markdown files (up to 12,000 characters) that enforce coding style, security mandates, and behavioral boundaries [6, 7]. They can be activated globally or per-workspace via manual `@mentions`, Always On configurations, Model Decision routing, or Glob patterns (e.g., `*.ts`) [7].
* **Workflows (Sequential Execution):** Action-oriented markdown files providing trajectory-level guidance [12]. Workflows are slash-invokable (e.g., `/workflow-name`) and nestable [4, 12]. The orchestrator can execute these step-by-step, or automatically generate them based on conversation history [13, 14].
* **Skills (Progressive Disclosure):** Isolated capabilities structured as a folder containing a `SKILL.md` file with YAML frontmatter (name, description) [15, 16]. Instead of flooding the context window, the agent reads only the description first, loading the full markdown body and associated scripts only when semantically relevant [17, 18].
* **Model Context Protocol (MCP):** Connects the agent to external tools and context [3]. Configured via `mcp_config.json`, MCP enables custom stdio or HTTP tools alongside an internal MCP Store with pre-built servers for databases and SaaS platforms [8, 10, 19].

Layer 2: Platform Implications & Orchestration

This architecture creates an environment where **capabilities are dynamically injected based on task-relevance rather than statically loaded**. The Agent Manager delegates tasks to sub-agents (Browser Subagent, Terminal Subagent) which inherit these localized constraints [20, 21]. Because Antigravity executes code natively on the host or via WSL2, Customization extends down to OS-level operations, controlled by Allowlist/Denylist policies for network routing and Strict Mode for sandboxed execution (Seatbelt on macOS, nsjail on Linux) [22-26].

Layer 3: Strategic Edge Cases & Scaling Risks

Under heavy orchestration, the system exhibits severe scaling and governance risks that require manual mitigation:

* **The Context Inversion Defect (R-P4):** Long-running workflows that inject the full `task_plan.md` on every tool call lack a pruning threshold. In sessions exceeding 60 tool calls, the plan itself exhausts the reasoning model's context window, degrading logic [27].
* **Phantom Phase Loops:** Workflows lack a "Phase Synchronicity Latch." If implementation state outpaces the `task_plan.md` record, the agent will loop on already-completed tasks [28].
* **mTLS and Secret Rotation Limitations:** Extensibility via MCP lacks native mTLS certificate fields in the `mcp_config.json` schema. Furthermore, secrets injected via the `env` block are static. Enterprise environments must front internal MCP servers with a reverse proxy (Envoy/nginx) to handle dynamic secret vaulting and mTLS termination [29, 30].

Risks & Mitigations

1. **Risk: Windows Infrastructure Governance Bypass**
2. _Issue:_ Lifecycle hooks (`.agents/hooks/*.sh`) are strictly Bash, failing silently on native Windows execution and dropping all commit-validation and planning locks [11].
3. _Mitigation:_ Port all 7 Bash hooks to dual-format, providing identical `.ps1` PowerShell scripts and update `AGENTS.md` to document per-OS hook dispatch [11].
4. **Risk: Master Identity Hallucination**
5. _Issue:_ The master `AGENTS.md` identity file frequently overstates capabilities (e.g., referencing a phantom "Awesome-Skills Pack (1,300+ skills)"). This causes the agent to hallucinate capabilities when it tries to invoke a non-existent file [31].
6. _Mitigation:_ Ensure `AGENTS.md` strictly references the physical contents of the `.agents/skills/` directory (e.g., ~48 curated skills) [31].
7. **Risk: Skill File Path Breakage**
8. _Issue:_ Skills using relative paths (`./resources/`) break when the agent's working directory differs from the skill folder [32].
9. _Mitigation:_ Mandate `file:///` absolute URIs for all resource pointers within `SKILL.md` implementations [32].

Deliverables

**1. Enterprise-Hardened Rule Template (Resolves Context Drift & Markdown Conflicts)** **workspace-rules.md**
    # ## ───── Boundary Constraints ─────
    # Replaces '---' dividers to prevent FSM Self-Audit collisions [33]
    1. Never bypass the Phase Synchronicity Latch: Every 5 tool calls, check file modification timestamps against `task_plan.md` [28].
    2. Plan Pruning Threshold: If `task_plan.md` exceeds 4,000 characters, summarize phases into `progress.md` and archive [27].
    3. Clean Code Contract: cyclomatic complexity ≤ 10, 100% JSDoc on APIs. Strict enforcement prior to GSD Verify [34].



**2. Standardized Skill Frontmatter & Pathing Template** **SKILL.md**
    ---
    name: "secure-api-auditor"
    description: "Audits REST/GraphQL APIs for OWASP Top 10 vulnerabilities. Triggers automatically on code modifications inside /routes or /controllers directories."
    ---
    # Instructions
    1. Discover endpoints via workspace symbol analysis.
    2. Cross-reference with the absolute URI resource: `file:///~/.gemini/antigravity/skills/secure-api-auditor/resources/owasp.md` [32].
    3. Generate an Artifact containing the audit report.



Recommended Next Actions

1. **Run an Extensibility Audit:** Check your `.agents/workflows/` directory for any duplicated callbacks (e.g., `notify_user`), and centralize them into a parameterized `bmad-task-executor.md` script to reduce technical debt [35].
2. **Check Hook Compatibility:** If running Windows without WSL2, immediately duplicate your `.sh` hooks to `.ps1` to restore governance gates [11].
3. **Define Escalation Triggers:** Review your Role Workflows (`pm.md`, `dev.md`) and insert mandatory `## Escalation Trigger` sections to block agents from switching personas (e.g., PM mutating code) without explicit user approval [36, 37].

Verification Checklist

* [x] Explored Rules, Workflows, Skills, and MCP components.
* [x] Identified underlying technical architecture and directory locations.
* [x] Highlighted edge cases, scalability issues, and OS-specific defects.
* [x] Provided copy-pasteable markdown/YAML artifacts enforcing platform best practices.


