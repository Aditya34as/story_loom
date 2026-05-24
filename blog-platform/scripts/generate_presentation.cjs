const pptxgen = require("pptxgenjs");

const pptx = new pptxgen();
pptx.layout = "LAYOUT_WIDE";
pptx.author = "OpenAI Codex";
pptx.company = "StoryLoom";
pptx.subject = "StoryLoom Project Presentation";
pptx.title = "StoryLoom - Blog Publishing Platform";
pptx.lang = "en-US";
pptx.theme = {
  headFontFace: "Aptos Display",
  bodyFontFace: "Aptos",
  lang: "en-US",
};

const C = {
  navy: "132238",
  teal: "1C6E6A",
  orange: "C65D2E",
  amber: "F3E6D7",
  cream: "FBF6EF",
  slate: "5A6677",
  light: "F7FAFC",
  dark: "0F172A",
  white: "FFFFFF",
  green: "1F7A4D",
  red: "AF3B3B",
  line: "D8E0E8",
};

function addBg(slide, variant = "light") {
  if (variant === "dark") {
    slide.background = { color: C.navy };
    slide.addShape(pptx.ShapeType.rect, {
      x: 0,
      y: 0,
      w: 13.333,
      h: 0.28,
      fill: { color: C.orange },
      line: { color: C.orange },
    });
  } else {
    slide.background = { color: C.cream };
    slide.addShape(pptx.ShapeType.rect, {
      x: 0,
      y: 0,
      w: 13.333,
      h: 0.18,
      fill: { color: C.orange },
      line: { color: C.orange },
    });
  }
}

function addTitle(slide, title, subtitle = "", opts = {}) {
  const color = opts.dark ? C.white : C.navy;
  slide.addText(title, {
    x: 0.65,
    y: 0.45,
    w: 8.8,
    h: 0.6,
    fontFace: "Aptos Display",
    fontSize: opts.big ? 28 : 22,
    bold: true,
    color,
    margin: 0,
  });
  if (subtitle) {
    slide.addText(subtitle, {
      x: 0.67,
      y: opts.big ? 1.2 : 1.0,
      w: 8.9,
      h: 0.45,
      fontSize: 10.5,
      color: opts.dark ? "D7E3F0" : C.slate,
      margin: 0,
    });
  }
}

function addFooter(slide, label) {
  slide.addText(label, {
    x: 0.65,
    y: 7.05,
    w: 4,
    h: 0.2,
    fontSize: 8.5,
    color: C.slate,
    margin: 0,
  });
}

function addBulletList(slide, items, x, y, w, h, opts = {}) {
  const runs = [];
  items.forEach((item) => {
    runs.push({
      text: item,
      options: {
        bullet: { indent: 14 },
        hanging: 2,
        breakLine: true,
      },
    });
  });
  slide.addText(runs, {
    x,
    y,
    w,
    h,
    fontSize: opts.fontSize || 16,
    color: opts.color || C.dark,
    paraSpaceAfterPt: opts.space || 8,
    valign: "top",
    margin: 0.04,
  });
}

function addSectionPill(slide, text, x = 0.68, y = 0.22, dark = false) {
  slide.addShape(pptx.ShapeType.roundRect, {
    x,
    y,
    w: 1.4 + text.length * 0.03,
    h: 0.28,
    rectRadius: 0.08,
    fill: { color: dark ? "24415F" : "E5F1F0" },
    line: { color: dark ? "24415F" : "E5F1F0" },
  });
  slide.addText(text, {
    x: x + 0.12,
    y: y + 0.05,
    w: 1.25 + text.length * 0.03,
    h: 0.15,
    fontSize: 8.5,
    bold: true,
    color: dark ? C.white : C.teal,
    margin: 0,
  });
}

function addMetricCard(slide, x, y, w, h, title, value, tone = "light") {
  slide.addShape(pptx.ShapeType.roundRect, {
    x, y, w, h,
    rectRadius: 0.08,
    fill: { color: tone === "dark" ? "21354F" : C.white, transparency: tone === "dark" ? 0 : 0 },
    line: { color: tone === "dark" ? "21354F" : C.line },
  });
  slide.addText(title, {
    x: x + 0.18,
    y: y + 0.2,
    w: w - 0.3,
    h: 0.22,
    fontSize: 9,
    color: tone === "dark" ? "D7E3F0" : C.slate,
    bold: true,
    margin: 0,
  });
  slide.addText(value, {
    x: x + 0.18,
    y: y + 0.42,
    w: w - 0.3,
    h: 0.45,
    fontSize: 22,
    bold: true,
    color: tone === "dark" ? C.white : C.navy,
    margin: 0,
  });
}

function addProcessBox(slide, x, y, w, h, title, body, fill) {
  slide.addShape(pptx.ShapeType.roundRect, {
    x, y, w, h,
    rectRadius: 0.06,
    fill: { color: fill },
    line: { color: fill },
  });
  slide.addText(title, {
    x: x + 0.12, y: y + 0.1, w: w - 0.24, h: 0.25,
    fontSize: 11.5, bold: true, color: C.navy, margin: 0,
  });
  slide.addText(body, {
    x: x + 0.12, y: y + 0.35, w: w - 0.24, h: h - 0.42,
    fontSize: 9.5, color: C.dark, margin: 0.02,
  });
}

// Slide 1
{
  const slide = pptx.addSlide();
  addBg(slide, "dark");
  slide.addShape(pptx.ShapeType.rect, {
    x: 8.8, y: 0.75, w: 3.7, h: 5.9,
    fill: { color: "1A304C" }, line: { color: "1A304C" },
  });
  slide.addShape(pptx.ShapeType.roundRect, {
    x: 9.4, y: 1.3, w: 2.5, h: 2.5,
    rectRadius: 0.12,
    fill: { color: C.orange }, line: { color: C.orange },
  });
  slide.addText("S", {
    x: 10.2, y: 1.72, w: 0.9, h: 0.8,
    fontSize: 34, bold: true, color: C.white, align: "center", margin: 0,
  });
  slide.addText("StoryLoom", {
    x: 0.72, y: 1.2, w: 5.8, h: 0.8,
    fontFace: "Aptos Display", fontSize: 28, bold: true, color: C.white, margin: 0,
  });
  slide.addText("A Blog Publishing and Content Management Platform", {
    x: 0.72, y: 2.0, w: 6.8, h: 0.8,
    fontSize: 24, bold: true, color: "F4F7FA", margin: 0,
  });
  slide.addText("Project Presentation", {
    x: 0.74, y: 2.85, w: 2.6, h: 0.35,
    fontSize: 14, bold: true, color: "BFD4E5", margin: 0,
  });
  slide.addText("Built using Laravel, MySQL, Blade, Tailwind CSS, and Vite", {
    x: 0.74, y: 3.3, w: 6.4, h: 0.42,
    fontSize: 13, color: "D8E4EE", margin: 0,
  });
  slide.addText("Prepared for classroom presentation and final project submission", {
    x: 0.74, y: 3.75, w: 6.6, h: 0.34,
    fontSize: 12, color: "D8E4EE", margin: 0,
  });
  slide.addText("Student Name: ____________________", {
    x: 0.75, y: 5.35, w: 3.8, h: 0.28, fontSize: 11, color: C.white, margin: 0,
  });
  slide.addText("Roll Number: ____________________", {
    x: 0.75, y: 5.65, w: 3.8, h: 0.28, fontSize: 11, color: C.white, margin: 0,
  });
  slide.addText("Guide / Teacher: ____________________", {
    x: 0.75, y: 5.95, w: 4.2, h: 0.28, fontSize: 11, color: C.white, margin: 0,
  });
}

// Slide 2 Agenda
{
  const slide = pptx.addSlide();
  addBg(slide);
  addSectionPill(slide, "AGENDA");
  addTitle(slide, "Presentation Roadmap", "This presentation explains the project from requirement analysis to implementation and testing.");
  addProcessBox(slide, 0.8, 1.55, 2.3, 1.1, "01. Introduction", "Problem statement, objective, and scope of the project", "FFF4E8");
  addProcessBox(slide, 3.3, 1.55, 2.3, 1.1, "02. Design", "Roles, modules, architecture, and database design", "EAF5F4");
  addProcessBox(slide, 5.8, 1.55, 2.3, 1.1, "03. Development", "How the system was built using Laravel and MySQL", "EEF2FF");
  addProcessBox(slide, 8.3, 1.55, 2.3, 1.1, "04. Working", "Public flow, writer dashboard, admin panel, and comments", "FFF4E8");
  addProcessBox(slide, 1.85, 3.15, 2.7, 1.1, "05. Validation", "Testing, verification, and problems solved during development", "EEF2FF");
  addProcessBox(slide, 5.1, 3.15, 2.7, 1.1, "06. Outcome", "Conclusion, future scope, and demo guidance", "EAF5F4");
  addBulletList(slide, [
    "The goal is to present not only the final website, but also the design thinking and implementation decisions behind it.",
    "Each section is structured so it can be explained clearly in class with minimal confusion."
  ], 0.95, 4.85, 11.2, 1.2, { fontSize: 15, color: C.slate });
  addFooter(slide, "StoryLoom Presentation");
}

// Slide 3 Problem statement
{
  const slide = pptx.addSlide();
  addBg(slide);
  addSectionPill(slide, "PROBLEM");
  addTitle(slide, "Problem Statement", "The project began with a simple but practical real-world requirement.");
  slide.addShape(pptx.ShapeType.roundRect, {
    x: 0.85, y: 1.55, w: 11.55, h: 1.5, rectRadius: 0.08,
    fill: { color: C.white }, line: { color: C.line },
  });
  slide.addText("\"A blog platform is required for writers to publish articles, manage content, and engage with their audience. The system should allow users to comment, share articles, and have an admin interface to manage posts.\"", {
    x: 1.1, y: 1.9, w: 11.0, h: 0.8,
    fontSize: 17, italic: true, color: C.navy, align: "center", valign: "mid", margin: 0,
  });
  addMetricCard(slide, 1.1, 3.55, 2.65, 1.25, "Core Need 1", "Publishing");
  addMetricCard(slide, 3.95, 3.55, 2.65, 1.25, "Core Need 2", "Engagement");
  addMetricCard(slide, 6.8, 3.55, 2.65, 1.25, "Core Need 3", "Moderation");
  addMetricCard(slide, 9.65, 3.55, 2.05, 1.25, "Goal", "Website");
  addBulletList(slide, [
    "The platform had to be more than a simple CRUD project. It needed real user roles, article visibility control, comments, and an admin interface.",
    "The website also had to look presentable enough for classroom demonstration and final submission."
  ], 0.95, 5.35, 11.1, 1.2, { fontSize: 15 });
  addFooter(slide, "Problem Definition");
}

// Slide 4 Objectives
{
  const slide = pptx.addSlide();
  addBg(slide);
  addSectionPill(slide, "OBJECTIVES");
  addTitle(slide, "Project Objectives", "The development plan was based on clear functional and presentation goals.");
  addBulletList(slide, [
    "Build a fully working Laravel blog platform with a professional website structure.",
    "Allow writers to create, edit, save drafts, and publish articles.",
    "Allow readers to browse published content and comment on articles.",
    "Provide administrators with control over posts, comments, and user roles.",
    "Use MySQL for proper database storage instead of temporary or mock storage.",
    "Design the UI with Tailwind CSS so the application looks clean and modern.",
    "Keep the implementation practical, understandable, and suitable for academic presentation."
  ], 0.9, 1.45, 7.2, 4.8, { fontSize: 17 });
  slide.addShape(pptx.ShapeType.roundRect, {
    x: 8.45, y: 1.55, w: 3.8, h: 4.7, rectRadius: 0.08,
    fill: { color: "FFF8F1" }, line: { color: "F3D8BE" },
  });
  slide.addText("Success Criteria", {
    x: 8.75, y: 1.9, w: 2.8, h: 0.28, fontSize: 18, bold: true, color: C.orange, margin: 0,
  });
  addBulletList(slide, [
    "Public homepage and article pages working correctly",
    "Writer dashboard managing real posts",
    "Admin panel controlling content",
    "Published posts visible only when valid",
    "Comments working with moderation",
    "Tests passing successfully"
  ], 8.7, 2.35, 3.0, 3.4, { fontSize: 14.5, color: C.dark, space: 7 });
  addFooter(slide, "Objectives of Development");
}

// Slide 5 scope and users
{
  const slide = pptx.addSlide();
  addBg(slide);
  addSectionPill(slide, "SCOPE");
  addTitle(slide, "Project Scope and Target Users", "The project was kept complete enough to be useful, but controlled enough to stay realistic.");
  addProcessBox(slide, 0.9, 1.55, 3.75, 2.1, "Reader Scope", "Browse published blog posts, open individual article pages, and comment on content after authentication.", "EEF8F7");
  addProcessBox(slide, 4.8, 1.55, 3.75, 2.1, "Writer Scope", "Create posts, edit posts, save draft posts, and publish content through a dedicated dashboard.", "FFF4E8");
  addProcessBox(slide, 8.7, 1.55, 3.75, 2.1, "Admin Scope", "Access platform overview, moderate comments, manage posts, and update user roles.", "EEF2FF");
  slide.addShape(pptx.ShapeType.roundRect, {
    x: 1.05, y: 4.25, w: 11.15, h: 1.65, rectRadius: 0.06,
    fill: { color: C.white }, line: { color: C.line },
  });
  slide.addText("Excluded from current scope:", {
    x: 1.35, y: 4.55, w: 2.3, h: 0.25, fontSize: 16, bold: true, color: C.red, margin: 0,
  });
  addBulletList(slide, [
    "No real-time notifications or chat",
    "No rich text editor",
    "No file-based image upload",
    "No category or tag filter module in this version",
    "No mobile app integration"
  ], 3.6, 4.43, 8.1, 1.05, { fontSize: 14.5, color: C.dark });
  addFooter(slide, "Scope Planning");
}

// Slide 6 stack
{
  const slide = pptx.addSlide();
  addBg(slide);
  addSectionPill(slide, "TECH STACK");
  addTitle(slide, "Technology Stack", "Each technology was selected to support a specific part of the project.");
  const rows = [
    [{ text: "Technology", options: { bold: true, color: C.white } }, { text: "Role in Project", options: { bold: true, color: C.white } }],
    ["Laravel 12", "Core PHP framework used for routing, controllers, models, middleware, migrations, and testing"],
    ["PHP 8.2", "Server-side programming language"],
    ["MySQL", "Main database for users, posts, comments, sessions, jobs, and cache tables"],
    ["Blade", "Templating engine used to create frontend pages and dashboards"],
    ["Tailwind CSS", "Utility-first CSS framework used to design the user interface"],
    ["Vite", "Frontend asset bundler used for CSS and JavaScript build process"],
    ["XAMPP", "Local MySQL and PHP development environment"],
  ];
  slide.addTable(rows, {
    x: 0.95, y: 1.45, w: 11.2, h: 4.25,
    border: { type: "solid", color: C.line, pt: 1 },
    fill: C.white,
    color: C.dark,
    rowH: 0.42,
    fontSize: 13.2,
    colW: [2.5, 8.7],
    margin: 0.08,
    autoFit: false,
    autoPage: false,
  });
  slide.addShape(pptx.ShapeType.rect, {
    x: 0.95, y: 1.45, w: 11.2, h: 0.42,
    fill: { color: C.navy }, line: { color: C.navy },
  });
  addFooter(slide, "Technology Choices");
}

// Slide 7 why stack
{
  const slide = pptx.addSlide();
  addBg(slide);
  addSectionPill(slide, "WHY THIS STACK");
  addTitle(slide, "Why Laravel, MySQL, and Tailwind?", "The choices were made for maintainability, speed of development, and presentation quality.");
  addProcessBox(slide, 0.95, 1.6, 3.8, 4.7, "Why Laravel?", "Laravel provides MVC structure, authentication support, routing, Eloquent ORM, migrations, middleware, and clean project organization. This made the system easier to build and easier to explain during presentation.", "EEF2FF");
  addProcessBox(slide, 4.8, 1.6, 3.8, 4.7, "Why MySQL?", "MySQL is widely used, reliable, and suitable for structured relational data. Since the project has users, posts, comments, and relationships between them, MySQL was a better permanent choice than local SQLite for final submission.", "FFF4E8");
  addProcessBox(slide, 8.65, 1.6, 3.7, 4.7, "Why Tailwind CSS?", "Tailwind CSS helped build a cleaner interface quickly while keeping the design consistent. It also made the Laravel frontend look more professional than plain default styling.", "EEF8F7");
  addFooter(slide, "Design Rationale");
}

// Slide 8 architecture
{
  const slide = pptx.addSlide();
  addBg(slide);
  addSectionPill(slide, "ARCHITECTURE");
  addTitle(slide, "System Architecture", "The application follows the MVC pattern supported by Laravel.");
  const boxes = [
    ["User / Browser", "Sends requests to access homepage, login, dashboard, and admin panel", 0.95, "EAF5F4"],
    ["Routes", "Routes map URLs to specific controllers and protect access using middleware", 3.5, "FFF4E8"],
    ["Controllers", "Controllers handle logic for authentication, posts, comments, and admin operations", 6.05, "EEF2FF"],
    ["Models", "Eloquent models interact with MySQL and manage relationships between tables", 8.6, "EAF5F4"],
  ];
  boxes.forEach(([title, body, x, fill]) => addProcessBox(slide, x, 2.05, 2.15, 1.85, title, body, fill));
  slide.addText("Request Flow", { x: 0.95, y: 4.45, w: 2, h: 0.25, fontSize: 17, bold: true, color: C.navy, margin: 0 });
  addBulletList(slide, [
    "Request enters through a route.",
    "Controller validates input and applies business logic.",
    "Model queries or updates MySQL database.",
    "Blade view renders HTML response.",
    "Tailwind CSS styles the final interface."
  ], 1.0, 4.8, 5.1, 1.7, { fontSize: 15 });
  slide.addShape(pptx.ShapeType.rightArrow, {
    x: 3.05, y: 2.68, w: 0.3, h: 0.25, fill: { color: C.orange }, line: { color: C.orange }
  });
  slide.addShape(pptx.ShapeType.rightArrow, {
    x: 5.6, y: 2.68, w: 0.3, h: 0.25, fill: { color: C.orange }, line: { color: C.orange }
  });
  slide.addShape(pptx.ShapeType.rightArrow, {
    x: 8.15, y: 2.68, w: 0.3, h: 0.25, fill: { color: C.orange }, line: { color: C.orange }
  });
  slide.addShape(pptx.ShapeType.roundRect, {
    x: 6.95, y: 4.65, w: 4.8, h: 1.4, rectRadius: 0.06,
    fill: { color: C.white }, line: { color: C.line }
  });
  slide.addText("Architecture Benefit", {
    x: 7.2, y: 4.95, w: 2.5, h: 0.2, fontSize: 16, bold: true, color: C.teal, margin: 0
  });
  slide.addText("This structure keeps the project organized, scalable, and easier to explain, debug, and extend.", {
    x: 7.2, y: 5.25, w: 4.15, h: 0.5, fontSize: 14.5, color: C.dark, margin: 0
  });
  addFooter(slide, "High-Level Architecture");
}

// Slide 9 modules
{
  const slide = pptx.addSlide();
  addBg(slide);
  addSectionPill(slide, "MODULES");
  addTitle(slide, "Main Project Modules", "The application was implemented in modular form so each responsibility is clearly separated.");
  const mod = [
    ["Authentication Module", "Registration, login, logout, and role-based redirection", 0.9, 1.55, "FFF4E8"],
    ["Public Blog Module", "Homepage, article list page, single article page, and share actions", 6.75, 1.55, "EEF8F7"],
    ["Writer Dashboard Module", "Create, edit, delete, draft, and publish posts", 0.9, 3.55, "EEF2FF"],
    ["Comment Module", "Authenticated users can comment; admin can moderate visibility", 6.75, 3.55, "FFF4E8"],
    ["Admin Management Module", "Overview metrics, post management, comment moderation, user role updates", 3.8, 5.55, "EEF8F7"],
  ];
  mod.forEach(([t, b, x, y, fill]) => addProcessBox(slide, x, y, 5.0, 1.45, t, b, fill));
  addFooter(slide, "Project Modules");
}

// Slide 10 roles
{
  const slide = pptx.addSlide();
  addBg(slide);
  addSectionPill(slide, "USER ROLES");
  addTitle(slide, "Role-Based Access Control", "Different user types are given different permissions inside the system.");
  addProcessBox(slide, 0.95, 1.55, 3.65, 4.9, "Reader", "Reader users can register, log in, browse published articles, and submit comments on published posts. They cannot access the writer or admin sections.", "EEF8F7");
  addProcessBox(slide, 4.85, 1.55, 3.65, 4.9, "Writer", "Writer users can access the dashboard, create posts, edit their own posts, save drafts, publish content, and remove posts they authored.", "FFF4E8");
  addProcessBox(slide, 8.75, 1.55, 3.65, 4.9, "Admin", "Admin users have the highest authority. They can access platform overview, manage all posts, hide or delete comments, and update user roles.", "EEF2FF");
  addFooter(slide, "Roles and Permissions");
}

// Slide 11 db overview
{
  const slide = pptx.addSlide();
  addBg(slide);
  addSectionPill(slide, "DATABASE");
  addTitle(slide, "Database Design Overview", "The application uses a relational MySQL database.");
  slide.addShape(pptx.ShapeType.roundRect, {
    x: 1.15, y: 1.85, w: 2.55, h: 2.3, rectRadius: 0.06,
    fill: { color: C.white }, line: { color: C.line }
  });
  slide.addText("users", { x: 1.35, y: 2.02, w: 1.2, h: 0.24, fontSize: 18, bold: true, color: C.navy, margin: 0 });
  addBulletList(slide, ["id", "name", "email", "role", "password"], 1.35, 2.35, 1.8, 1.2, { fontSize: 13.5 });
  slide.addShape(pptx.ShapeType.roundRect, {
    x: 5.4, y: 1.85, w: 2.55, h: 2.6, rectRadius: 0.06,
    fill: { color: C.white }, line: { color: C.line }
  });
  slide.addText("posts", { x: 5.62, y: 2.02, w: 1.2, h: 0.24, fontSize: 18, bold: true, color: C.navy, margin: 0 });
  addBulletList(slide, ["id", "user_id", "title", "slug", "excerpt", "content", "status", "published_at"], 5.62, 2.35, 2.0, 1.6, { fontSize: 13.5 });
  slide.addShape(pptx.ShapeType.roundRect, {
    x: 9.6, y: 1.85, w: 2.55, h: 2.3, rectRadius: 0.06,
    fill: { color: C.white }, line: { color: C.line }
  });
  slide.addText("comments", { x: 9.8, y: 2.02, w: 1.6, h: 0.24, fontSize: 18, bold: true, color: C.navy, margin: 0 });
  addBulletList(slide, ["id", "post_id", "user_id", "comment", "status"], 9.8, 2.35, 1.9, 1.15, { fontSize: 13.5 });
  slide.addShape(pptx.ShapeType.line, { x: 3.7, y: 2.95, w: 1.65, h: 0, line: { color: C.orange, pt: 2, beginArrowType: "none", endArrowType: "triangle" } });
  slide.addShape(pptx.ShapeType.line, { x: 7.95, y: 2.95, w: 1.65, h: 0, line: { color: C.orange, pt: 2, beginArrowType: "none", endArrowType: "triangle" } });
  addBulletList(slide, [
    "One user can create many posts.",
    "One user can create many comments.",
    "One post can have many comments.",
    "All primary content is stored in MySQL."
  ], 1.1, 5.15, 10.7, 1.1, { fontSize: 15 });
  addFooter(slide, "Core Entity Design");
}

// Slide 12 migrations & schema logic
{
  const slide = pptx.addSlide();
  addBg(slide);
  addSectionPill(slide, "SCHEMA");
  addTitle(slide, "Schema and Migration Strategy", "Laravel migrations were used to create and maintain database structure in a controlled way.");
  addBulletList(slide, [
    "The users table was created first using Laravel default migration, then expanded by adding the custom role field.",
    "A dedicated posts table was created with author reference, title, slug, excerpt, content, image URL, status, and published timestamp.",
    "A comments table was created with foreign key links to both users and posts.",
    "Cascade delete rules were applied so orphan data is avoided when users or posts are removed.",
    "Laravel migration files make the database reproducible on any local machine."
  ], 0.95, 1.45, 6.85, 3.9, { fontSize: 16 });
  slide.addShape(pptx.ShapeType.roundRect, {
    x: 8.05, y: 1.6, w: 4.0, h: 3.95, rectRadius: 0.06,
    fill: { color: C.white }, line: { color: C.line }
  });
  slide.addText("Implemented Migration Files", {
    x: 8.3, y: 1.88, w: 2.9, h: 0.24, fontSize: 16.5, bold: true, color: C.orange, margin: 0
  });
  addBulletList(slide, [
    "create_users_table",
    "add_role_to_users_table",
    "create_posts_table",
    "create_comments_table",
    "create_cache_table",
    "create_jobs_table"
  ], 8.25, 2.2, 3.35, 2.6, { fontSize: 14 });
  addFooter(slide, "Migration-Based Database Setup");
}

// Slide 13 routing
{
  const slide = pptx.addSlide();
  addBg(slide);
  addSectionPill(slide, "ROUTES");
  addTitle(slide, "Routing Structure", "Routes were divided according to public, authenticated, writer, and admin sections.");
  const tableRows = [
    [{ text: "Route Group", options: { bold: true, color: C.white } }, { text: "Examples", options: { bold: true, color: C.white } }, { text: "Purpose", options: { bold: true, color: C.white } }],
    ["Public", "/, /posts, /posts/{slug}", "Display homepage, article listing, and single article pages"],
    ["Guest Only", "/login, /register", "Allow new or logged out users to enter the system"],
    ["Authenticated", "/logout, /posts/{post}/comments", "Allow signed-in users to log out and post comments"],
    ["Writer + Admin", "/dashboard/posts, /dashboard/posts/create", "Manage post creation and editing"],
    ["Admin Only", "/admin, /admin/comments, /admin/users", "Platform moderation and oversight"],
  ];
  slide.addTable(tableRows, {
    x: 0.85, y: 1.55, w: 11.7, h: 4.0,
    border: { type: "solid", color: C.line, pt: 1 },
    fill: C.white, color: C.dark, fontSize: 13.2,
    colW: [2.0, 3.8, 5.9], rowH: 0.48, margin: 0.08,
  });
  slide.addShape(pptx.ShapeType.rect, {
    x: 0.85, y: 1.55, w: 11.7, h: 0.44, fill: { color: C.navy }, line: { color: C.navy }
  });
  addFooter(slide, "Route Grouping");
}

// Slide 14 public flow
{
  const slide = pptx.addSlide();
  addBg(slide);
  addSectionPill(slide, "PUBLIC FLOW");
  addTitle(slide, "How the Public Blog Works", "Only valid published posts are visible to readers.");
  addProcessBox(slide, 0.85, 2.0, 2.1, 1.65, "Step 1", "Homepage requests latest published posts from MySQL", "EEF8F7");
  addProcessBox(slide, 3.15, 2.0, 2.1, 1.65, "Step 2", "Article listing page paginates only published posts", "FFF4E8");
  addProcessBox(slide, 5.45, 2.0, 2.1, 1.65, "Step 3", "Single post page loads author, comments, and related posts", "EEF2FF");
  addProcessBox(slide, 7.75, 2.0, 2.1, 1.65, "Step 4", "Share buttons allow link distribution for audience engagement", "EEF8F7");
  addProcessBox(slide, 10.05, 2.0, 2.1, 1.65, "Step 5", "Logged-in readers can comment on published content", "FFF4E8");
  slide.addShape(pptx.ShapeType.line, { x: 2.95, y: 2.8, w: 0.18, h: 0, line: { color: C.orange, pt: 2, endArrowType: "triangle" } });
  slide.addShape(pptx.ShapeType.line, { x: 5.25, y: 2.8, w: 0.18, h: 0, line: { color: C.orange, pt: 2, endArrowType: "triangle" } });
  slide.addShape(pptx.ShapeType.line, { x: 7.55, y: 2.8, w: 0.18, h: 0, line: { color: C.orange, pt: 2, endArrowType: "triangle" } });
  slide.addShape(pptx.ShapeType.line, { x: 9.85, y: 2.8, w: 0.18, h: 0, line: { color: C.orange, pt: 2, endArrowType: "triangle" } });
  addBulletList(slide, [
    "The application uses a `published()` scope so draft posts remain hidden from the public pages.",
    "This ensures that the writer dashboard can contain unfinished content without exposing it to readers."
  ], 1.0, 4.8, 11.0, 1.1, { fontSize: 15.5 });
  addFooter(slide, "Public Reader Journey");
}

// Slide 15 writer flow
{
  const slide = pptx.addSlide();
  addBg(slide);
  addSectionPill(slide, "WRITER FLOW");
  addTitle(slide, "Writer Dashboard Workflow", "This is the main content creation area of the project.");
  addBulletList(slide, [
    "Writer logs in and enters the post dashboard.",
    "Writer opens the create post form.",
    "Writer enters title, excerpt, content, image URL, and status.",
    "Laravel validates the form data.",
    "A unique slug is generated automatically from the title.",
    "If the status is set to published, the `published_at` value is stored automatically.",
    "Writer can later edit or delete the post from the dashboard."
  ], 0.95, 1.55, 6.5, 4.4, { fontSize: 16 });
  slide.addShape(pptx.ShapeType.roundRect, {
    x: 7.9, y: 1.75, w: 4.1, h: 3.9, rectRadius: 0.06,
    fill: { color: C.white }, line: { color: C.line }
  });
  slide.addText("Key Implementation Logic", {
    x: 8.2, y: 2.0, w: 2.9, h: 0.24, fontSize: 16.5, bold: true, color: C.teal, margin: 0
  });
  addBulletList(slide, [
    "Form validation for title, excerpt, content, image URL, and status",
    "Slug uniqueness handling",
    "Author ownership check before edit/delete",
    "Draft vs Published state tracking",
    "Published timestamp assignment"
  ], 8.1, 2.35, 3.3, 2.8, { fontSize: 14 });
  addFooter(slide, "Writer Operations");
}

// Slide 16 admin flow
{
  const slide = pptx.addSlide();
  addBg(slide);
  addSectionPill(slide, "ADMIN FLOW");
  addTitle(slide, "Admin Panel Workflow", "The admin section provides platform-level control and moderation.");
  addProcessBox(slide, 0.95, 1.7, 2.35, 2.3, "Overview Dashboard", "Shows metrics such as total posts, published posts, drafts, comments, and active writers.", "FFF4E8");
  addProcessBox(slide, 3.55, 1.7, 2.35, 2.3, "Post Management", "Admin can list all posts and remove posts when needed.", "EEF8F7");
  addProcessBox(slide, 6.15, 1.7, 2.35, 2.3, "Comment Moderation", "Admin can hide, show, or delete comments from reader discussions.", "EEF2FF");
  addProcessBox(slide, 8.75, 1.7, 2.35, 2.3, "User Role Management", "Admin can change user roles between reader, writer, and admin.", "EEF8F7");
  addBulletList(slide, [
    "This module makes the website practical for real use, because content platforms need moderation and role management.",
    "Without admin control, even a functional blogging platform would remain incomplete from a management perspective."
  ], 1.0, 4.55, 10.8, 1.15, { fontSize: 15.5, color: C.slate });
  addFooter(slide, "Admin Management");
}

// Slide 17 implementation details
{
  const slide = pptx.addSlide();
  addBg(slide);
  addSectionPill(slide, "IMPLEMENTATION");
  addTitle(slide, "Important Implementation Decisions", "Some logic decisions were especially important for making the system behave correctly.");
  addProcessBox(slide, 0.9, 1.55, 3.7, 1.55, "Published Scope Logic", "Public pages query only posts with status = published, a non-null published_at value, and a publish date not in the future.", "EEF8F7");
  addProcessBox(slide, 4.8, 1.55, 3.7, 1.55, "Role Middleware", "Writer and admin routes are protected using role checks so unauthorized users cannot access restricted areas.", "FFF4E8");
  addProcessBox(slide, 8.7, 1.55, 3.7, 1.55, "Slug Generation", "Post slugs are generated automatically and uniqueness is preserved even when titles are similar.", "EEF2FF");
  addProcessBox(slide, 0.9, 3.45, 3.7, 1.55, "Ownership Protection", "Writers can edit only their own posts, while admin has platform-wide access.", "FFF4E8");
  addProcessBox(slide, 4.8, 3.45, 3.7, 1.55, "Comment Moderation", "Comments are visible by default but can be hidden or deleted by admin to keep discussion clean.", "EEF8F7");
  addProcessBox(slide, 8.7, 3.45, 3.7, 1.55, "MySQL Migration Shift", "The project was fully moved from SQLite to MySQL, including runtime configuration and test database setup.", "EEF2FF");
  addFooter(slide, "Core Logic Decisions");
}

// Slide 18 UI and design
{
  const slide = pptx.addSlide();
  addBg(slide);
  addSectionPill(slide, "UI DESIGN");
  addTitle(slide, "Frontend Design and User Experience", "The interface was redesigned with Tailwind CSS to make the project look like a complete website.");
  addBulletList(slide, [
    "A branded visual identity was created around the StoryLoom name.",
    "The homepage includes a featured section and latest article cards.",
    "Writers and admins have dedicated dashboard interfaces instead of plain default pages.",
    "The design uses responsive layouts so the UI remains usable on different screen sizes.",
    "Buttons, cards, panels, forms, and tables follow a consistent visual language.",
    "The overall goal was to make the project feel presentation-ready, not just technically functional."
  ], 0.95, 1.45, 6.9, 4.7, { fontSize: 16 });
  slide.addShape(pptx.ShapeType.roundRect, {
    x: 8.0, y: 1.65, w: 4.0, h: 4.4, rectRadius: 0.06,
    fill: { color: C.white }, line: { color: C.line }
  });
  slide.addText("Main UI Areas", {
    x: 8.3, y: 1.95, w: 2.4, h: 0.22, fontSize: 16.5, bold: true, color: C.orange, margin: 0
  });
  addBulletList(slide, [
    "Homepage",
    "Article listing page",
    "Single post page",
    "Login & registration pages",
    "Writer dashboard",
    "Admin dashboard",
    "Comments section"
  ], 8.2, 2.3, 3.0, 2.8, { fontSize: 14.5 });
  addFooter(slide, "Tailwind UI Layer");
}

// Slide 19 security and validation
{
  const slide = pptx.addSlide();
  addBg(slide);
  addSectionPill(slide, "SECURITY");
  addTitle(slide, "Security, Validation, and Data Safety", "Even for an academic project, basic safeguards were added to keep the system reliable.");
  const rows = [
    [{ text: "Area", options: { bold: true, color: C.white } }, { text: "Implementation", options: { bold: true, color: C.white } }],
    ["Authentication", "Users must log in to comment, manage posts, or access admin pages"],
    ["Role Protection", "Writer and admin sections use route middleware"],
    ["Validation", "Post and comment forms are validated before storing data"],
    ["Ownership Checks", "Writers cannot edit or delete another writer's posts"],
    ["Secrets Safety", ".env is ignored and .env.example is provided for GitHub"],
    ["Database Safety", "MySQL structure is controlled through migrations and seeders"],
  ];
  slide.addTable(rows, {
    x: 1.0, y: 1.55, w: 11.1, h: 3.75,
    border: { type: "solid", color: C.line, pt: 1 },
    fill: C.white, color: C.dark, fontSize: 13.4,
    colW: [2.4, 8.7], rowH: 0.46, margin: 0.08,
  });
  slide.addShape(pptx.ShapeType.rect, {
    x: 1.0, y: 1.55, w: 11.1, h: 0.44, fill: { color: C.navy }, line: { color: C.navy }
  });
  addFooter(slide, "Protection and Reliability");
}

// Slide 20 how it was built
{
  const slide = pptx.addSlide();
  addBg(slide);
  addSectionPill(slide, "BUILD PROCESS");
  addTitle(slide, "How the Project Was Built", "This slide is useful when the teacher asks for development process rather than only final output.");
  addProcessBox(slide, 0.9, 1.65, 2.2, 1.35, "Step 1", "Created a fresh Laravel project structure and configured environment setup.", "EEF2FF");
  addProcessBox(slide, 3.25, 1.65, 2.2, 1.35, "Step 2", "Designed the data model for users, posts, comments, and roles.", "FFF4E8");
  addProcessBox(slide, 5.6, 1.65, 2.2, 1.35, "Step 3", "Implemented controllers, models, routes, and middleware.", "EEF8F7");
  addProcessBox(slide, 7.95, 1.65, 2.2, 1.35, "Step 4", "Built public blog pages, writer dashboard, and admin panel.", "EEF2FF");
  addProcessBox(slide, 10.3, 1.65, 2.2, 1.35, "Step 5", "Connected the UI to Tailwind CSS and built frontend assets.", "FFF4E8");
  addBulletList(slide, [
    "After the functional version was ready, the application was moved from SQLite to proper MySQL.",
    "The final stage focused on testing, fixing visibility issues, cleaning GitHub safety files, and preparing documentation."
  ], 1.0, 3.65, 11.0, 1.2, { fontSize: 15.5 });
  addFooter(slide, "Development Method");
}

// Slide 21 testing
{
  const slide = pptx.addSlide();
  addBg(slide);
  addSectionPill(slide, "TESTING");
  addTitle(slide, "Testing and Verification", "The project was checked both functionally and through Laravel tests.");
  addProcessBox(slide, 0.95, 1.6, 3.5, 4.2, "Functional Verification", "The following flows were checked manually:\n\n• Registration\n• Login and logout\n• Writer post creation\n• Draft vs published handling\n• Reader comments\n• Admin moderation\n• Public visibility of posts", "EEF8F7");
  addProcessBox(slide, 4.9, 1.6, 3.5, 4.2, "Database Verification", "MySQL configuration was verified for both the main application database and the testing database.\n\n• storyloom\n• storyloom_testing\n\nOld SQLite configuration and file usage were removed.", "FFF4E8");
  addProcessBox(slide, 8.85, 1.6, 3.5, 4.2, "Automated Verification", "Laravel test suite was run successfully after the MySQL transition.\n\nCommand used:\n\nphp artisan test\n\nThis confirmed routes and basic public pages were still working.", "EEF2FF");
  addFooter(slide, "Quality Assurance");
}

// Slide 22 challenges
{
  const slide = pptx.addSlide();
  addBg(slide);
  addSectionPill(slide, "CHALLENGES");
  addTitle(slide, "Challenges Faced and Solutions Applied", "Explaining these points makes the presentation stronger because it shows engineering decisions, not only output.");
  const rows = [
    [{ text: "Challenge", options: { bold: true, color: C.white } }, { text: "Solution Applied", options: { bold: true, color: C.white } }],
    ["Initial setup from empty workspace", "Scaffolded a fresh Laravel application and built the project structure step by step"],
    ["UI looked too basic", "Rebuilt the interface using Tailwind CSS and Vite"],
    ["Switching from SQLite to MySQL", "Updated environment, config files, tests, and removed SQLite leftovers"],
    ["Published blog not appearing publicly", "Verified that public pages depend on published posts stored in the active MySQL database"],
    ["GitHub safety concerns", "Checked .gitignore, .env.example, build files, and test configuration"],
  ];
  slide.addTable(rows, {
    x: 0.9, y: 1.55, w: 11.4, h: 4.2,
    border: { type: "solid", color: C.line, pt: 1 },
    fill: C.white, color: C.dark, fontSize: 13.2,
    colW: [3.8, 7.6], rowH: 0.62, margin: 0.08,
  });
  slide.addShape(pptx.ShapeType.rect, {
    x: 0.9, y: 1.55, w: 11.4, h: 0.44, fill: { color: C.navy }, line: { color: C.navy }
  });
  addFooter(slide, "Practical Problems Solved");
}

// Slide 23 demo
{
  const slide = pptx.addSlide();
  addBg(slide);
  addSectionPill(slide, "DEMO GUIDE");
  addTitle(slide, "How to Demonstrate the Project in Class", "This slide can act as your own speaking plan during the live demo.");
  addBulletList(slide, [
    "Start with the homepage and explain the purpose of the platform.",
    "Open the article listing page and show that only published posts are visible.",
    "Open a single post page and show comments plus article sharing section.",
    "Login as writer and show the writer dashboard.",
    "Create or edit a post and explain draft vs published behavior.",
    "Login as admin and show comment moderation and role management.",
    "Conclude by summarizing the technologies and database setup."
  ], 0.95, 1.45, 7.2, 4.8, { fontSize: 16 });
  slide.addShape(pptx.ShapeType.roundRect, {
    x: 8.35, y: 1.65, w: 3.8, h: 4.45, rectRadius: 0.06,
    fill: { color: C.white }, line: { color: C.line }
  });
  slide.addText("Demo Accounts", {
    x: 8.65, y: 1.95, w: 2.4, h: 0.24, fontSize: 16.5, bold: true, color: C.orange, margin: 0
  });
  addBulletList(slide, [
    "Admin\nadmin@storyloom.test\npassword",
    "Writer\nwriter@storyloom.test\npassword",
    "Reader\nreader@storyloom.test\npassword"
  ], 8.55, 2.3, 2.95, 2.9, { fontSize: 14.2, space: 14 });
  addFooter(slide, "Live Demo Sequence");
}

// Slide 24 future scope
{
  const slide = pptx.addSlide();
  addBg(slide);
  addSectionPill(slide, "FUTURE SCOPE");
  addTitle(slide, "Future Enhancements", "The current version is complete for submission, but it can be extended further.");
  addMetricCard(slide, 0.95, 1.75, 2.2, 1.15, "Enhancement 1", "Categories");
  addMetricCard(slide, 3.35, 1.75, 2.2, 1.15, "Enhancement 2", "Search");
  addMetricCard(slide, 5.75, 1.75, 2.2, 1.15, "Enhancement 3", "Image Upload");
  addMetricCard(slide, 8.15, 1.75, 2.2, 1.15, "Enhancement 4", "Profiles");
  addMetricCard(slide, 10.55, 1.75, 1.8, 1.15, "Enhancement 5", "Analytics");
  addBulletList(slide, [
    "Rich text editor for writers",
    "Category and tag management",
    "Search and filtering",
    "File upload for images instead of URL-based input",
    "Bookmarks, likes, and personalized reader features",
    "Advanced admin analytics and editorial workflow"
  ], 1.0, 3.35, 11.0, 2.1, { fontSize: 16 });
  addFooter(slide, "Possible Extensions");
}

// Slide 25 conclusion
{
  const slide = pptx.addSlide();
  addBg(slide, "dark");
  addSectionPill(slide, "CONCLUSION", 0.72, 0.22, true);
  addTitle(slide, "Conclusion", "StoryLoom successfully addresses the full problem statement through a role-based Laravel web application.", { dark: true, big: true });
  addBulletList(slide, [
    "Writers can publish and manage content.",
    "Readers can browse and engage through comments.",
    "Admins can moderate the platform effectively.",
    "MySQL provides proper structured storage.",
    "Tailwind CSS helps the project look presentation-ready.",
    "The final system is suitable for both demonstration and academic submission."
  ], 0.95, 1.75, 6.8, 3.5, { fontSize: 18, color: C.white });
  slide.addShape(pptx.ShapeType.roundRect, {
    x: 8.25, y: 1.55, w: 4.2, h: 4.6, rectRadius: 0.08,
    fill: { color: "1C304A" }, line: { color: "1C304A" }
  });
  slide.addText("Thank You", {
    x: 9.15, y: 2.35, w: 2.3, h: 0.5, fontSize: 28, bold: true, color: C.white, align: "center", margin: 0
  });
  slide.addText("Questions & Discussion", {
    x: 8.85, y: 3.0, w: 2.9, h: 0.35, fontSize: 16, color: "D8E4EE", align: "center", margin: 0
  });
  slide.addText("StoryLoom", {
    x: 9.15, y: 4.5, w: 2.3, h: 0.35, fontSize: 18, bold: true, color: C.orange, align: "center", margin: 0
  });
}

pptx.writeFile({ fileName: "StoryLoom_Project_Presentation.pptx" });
