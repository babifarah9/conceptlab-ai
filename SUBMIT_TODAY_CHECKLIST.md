# Submit-Today Checklist

## Must have
- [ ] Join/register for the OpenAI Build Week challenge on Devpost
- [ ] Put these files into a GitHub repository
- [ ] Add `.env` to `.gitignore`
- [ ] Run the application locally
- [ ] Test lesson generation
- [ ] Test Teach Back evaluation
- [ ] Test Publish Learning Card
- [ ] Replace placeholders in `DEVPOST_SUBMISSION.md`
- [ ] Record a public YouTube demo under 3 minutes
- [ ] Obtain the Codex `/feedback` session ID
- [ ] Submit under **Education**

## Git commands
```bash
git init
git add .
git commit -m "Build ConceptLab AI MVP"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## Recommended repository settings
- Public repository
- Add an MIT license
- Add one screenshot or GIF near the top of README
- Do not commit `.env` or API keys

## Fast local test
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# edit .env
uvicorn app:app --reload
```

## Submission order
1. Make the core flow work.
2. Push the repository.
3. Record the demo.
4. Upload to YouTube as Public.
5. Paste the prepared Devpost copy.
6. Add repository, demo, deployed-app, and `/feedback` values.
7. Submit before the deadline.

## Do not spend today's time on
- Full authentication
- Payments
- Complex dashboards
- Real-time collaboration
- Executing arbitrary generated code
- Native mobile apps
- A large database schema
