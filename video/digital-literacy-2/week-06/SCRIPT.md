## Define one useful task
Start with a small problem: help someone find a fictional community resource. Keep the first app to one page with search, a category filter, and readable results. Write three checks before asking AI to build anything, so you can tell whether the result actually works.

## Understand the parts
HTML gives the page its content and structure. CSS controls appearance and layout. JavaScript responds to input, such as filtering a list. The supplied starter keeps fictional records inside the file. It has no real account system, private database, or payment service.

## Give a bounded prompt
Tell the AI what the user should do, which controls are needed, and how to test them. Ask for labeled fields, visible keyboard focus, and no external dependencies. Use fictional data. Do not place passwords or private API keys in browser code, because people can inspect that code.

## Test before you trust
Run the checks yourself. Try a matching name, a search with no results, and different letter cases. Use only the keyboard, then narrow the screen. Record what you expected and what actually happened. A confident AI statement does not count as evidence that these paths work.

## Revise, then check again
Save a first version, request or make one small improvement, and repeat the affected test. Also repeat a test that already passed to catch a new problem. If no AI tool is available, edit the starter's heading and a fictional resource in a plain-text editor. Keep both versions and your test log.