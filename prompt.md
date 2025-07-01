
**CONTEXT**: I need a cross-platform Obsidian MOC automation system that works seamlessly across different computers, operating systems, and vault locations with GitHub synchronization.

**OBJECTIVE**: Create a complete daily automation solution that generates Maps of Content (MOCs) automatically without manual intervention.

**SPECIFIC REQUIREMENTS**:

### Core Functionality
- **Daily automated MOC generation** for new notes and folders
- **Cross-platform compatibility** (Windows, macOS, Linux)
- **Dynamic vault location detection** (handles moves, clones, different computers)
- **GitHub sync integration** (works with repository synchronization)

### Technical Specifications
- **Programming language**: Python (for cross-platform compatibility)
- **Scheduling**: Native OS schedulers (Task Scheduler, cron, launchd)
- **Configuration**: Auto-detection with manual override options
- **Error handling**: Comprehensive logging and recovery mechanisms

### Documentation Requirements
- **Target audience**: Complete beginners (19-year-old level explanation)
- **Structure**: Step-by-step instructions embedded within code files
- **Coverage**: Installation, configuration, troubleshooting for each OS
- **Location**: New folder named "Automation" inside Projects directory

### Deliverables
1. **Main automation script** with vault auto-detection
2. **OS-specific setup scripts** (Windows PowerShell, macOS/Linux Bash)
3. **Installation automation** for each operating system
4. **Comprehensive documentation** with troubleshooting guides
5. **Configuration management** system for different environments

### Success Criteria
- **Zero manual configuration** after initial setup
- **Works immediately** after cloning vault to new computer
- **Handles OS switches** without reconfiguration
- **Beginner-friendly** setup process under 15 minutes
- **Robust error handling** with clear error messages

**CONSTRAINTS**: 
- Must work offline after initial setup
- Should not require admin privileges for daily operation
- Must preserve existing vault structure and files
- Should handle large vaults (1000+ notes) efficiently

**OUTPUT FORMAT**: Complete file structure with embedded documentation, ready-to-deploy scripts, and foolproof installation instructions.
