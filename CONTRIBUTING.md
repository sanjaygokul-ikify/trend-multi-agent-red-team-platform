### Contribution Workflow
1. Create a feature branch from main
2. Implement changes with full CI coverage
3. Submit RFC for architectural decisions >50 lines
4. Squash-merge after code review
5. Update CHANGELOG.md with semantic versioning

### Security
All PRs must pass
- Bandit security analysis
- FauxPas code style
- 100% unit test coverage
- Dependency graph scan