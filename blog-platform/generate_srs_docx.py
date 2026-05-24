"""
Generate StoryLoom SRS Report as a Word .docx file.
"""

from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml
import os

doc = Document()

# ─── Page Setup ───
for section in doc.sections:
    section.top_margin = Cm(2.54)
    section.bottom_margin = Cm(2.54)
    section.left_margin = Cm(2.54)
    section.right_margin = Cm(2.54)

style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(12)
style.paragraph_format.line_spacing = 1.5

# ─── Helper Functions ───
def set_cell_shading(cell, color):
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color}"/>')
    cell._tc.get_or_add_tcPr().append(shading)

def add_styled_table(doc, headers, rows, col_widths=None, header_color="2d2d44"):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Header row
    for i, header in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = ''
        p = cell.paragraphs[0]
        run = p.add_run(header)
        run.bold = True
        run.font.size = Pt(10.5)
        run.font.color.rgb = RGBColor(255, 255, 255)
        run.font.name = 'Times New Roman'
        set_cell_shading(cell, header_color)

    # Data rows
    for r_idx, row in enumerate(rows):
        for c_idx, val in enumerate(row):
            cell = table.rows[r_idx + 1].cells[c_idx]
            cell.text = ''
            p = cell.paragraphs[0]
            run = p.add_run(str(val))
            run.font.size = Pt(10.5)
            run.font.name = 'Times New Roman'
            if r_idx % 2 == 1:
                set_cell_shading(cell, "f5f5fa")

    return table

def heading1(text):
    h = doc.add_heading(text, level=1)
    for run in h.runs:
        run.font.color.rgb = RGBColor(0x1a, 0x1a, 0x2e)
        run.font.name = 'Times New Roman'
    return h

def heading2(text):
    h = doc.add_heading(text, level=2)
    for run in h.runs:
        run.font.color.rgb = RGBColor(0x2d, 0x2d, 0x44)
        run.font.name = 'Times New Roman'
    return h

def heading3(text):
    h = doc.add_heading(text, level=3)
    for run in h.runs:
        run.font.color.rgb = RGBColor(0x3a, 0x3a, 0x5c)
        run.font.name = 'Times New Roman'
    return h

def heading4(text):
    h = doc.add_heading(text, level=4)
    for run in h.runs:
        run.font.color.rgb = RGBColor(0x44, 0x44, 0x44)
        run.font.name = 'Times New Roman'
    return h

def para(text, bold=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY):
    p = doc.add_paragraph()
    p.alignment = align
    run = p.add_run(text)
    run.bold = bold
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    return p

def bullet(text, level=0):
    p = doc.add_paragraph(style='List Bullet')
    p.clear()
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    if level > 0:
        p.paragraph_format.left_indent = Cm(1.27 * level)
    return p

def numbered(text):
    p = doc.add_paragraph(style='List Number')
    p.clear()
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    return p

def add_page_break():
    doc.add_page_break()

def bold_para(text, rest=""):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r1 = p.add_run(text)
    r1.bold = True
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(12)
    if rest:
        r2 = p.add_run(rest)
        r2.font.name = 'Times New Roman'
        r2.font.size = Pt(12)
    return p


# ══════════════════════════════════════════════════════════════════════
# COVER PAGE
# ══════════════════════════════════════════════════════════════════════

for _ in range(4):
    doc.add_paragraph()

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('StoryLoom')
run.bold = True
run.font.size = Pt(28)
run.font.color.rgb = RGBColor(0x1a, 0x1a, 0x2e)
run.font.name = 'Times New Roman'

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('Software Requirements Specification')
run.bold = True
run.font.size = Pt(20)
run.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
run.font.name = 'Times New Roman'

doc.add_paragraph()

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('CS / SE Course\nSoftware Engineering')
run.font.size = Pt(14)
run.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
run.font.name = 'Times New Roman'

doc.add_paragraph()

# Info table on cover page
info_table = doc.add_table(rows=5, cols=2)
info_table.style = 'Table Grid'
info_table.alignment = WD_TABLE_ALIGNMENT.CENTER

info_data = [
    ("Project Name", "StoryLoom – Blog Publishing Platform"),
    ("Student Name(s)", "1. Aditya Sharma\n2. Rahul Verma\n3. Priya Gupta"),
    ("Registration Number(s)", "1. 22BCSE01\n2. 22BCSE02\n3. 22BCSE03"),
    ("Document Version", "1.0"),
    ("Date", "24 May 2025"),
]
for i, (label, value) in enumerate(info_data):
    cell_l = info_table.rows[i].cells[0]
    cell_l.text = ''
    run_l = cell_l.paragraphs[0].add_run(label)
    run_l.bold = True
    run_l.font.size = Pt(11)
    run_l.font.name = 'Times New Roman'
    set_cell_shading(cell_l, "e8e8f0")

    cell_r = info_table.rows[i].cells[1]
    cell_r.text = ''
    run_r = cell_r.paragraphs[0].add_run(value)
    run_r.font.size = Pt(11)
    run_r.font.name = 'Times New Roman'

doc.add_paragraph()
doc.add_paragraph()

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('Prepared for')
run.bold = True
run.font.size = Pt(13)
run.font.name = 'Times New Roman'

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('Continuous Assessment 3\nSpring 2025')
run.font.size = Pt(13)
run.font.name = 'Times New Roman'

add_page_break()

# ══════════════════════════════════════════════════════════════════════
# REVISION HISTORY
# ══════════════════════════════════════════════════════════════════════
heading1('REVISION HISTORY')
add_styled_table(doc,
    ["Version", "Date", "Author", "Description"],
    [["1.0", "24-May-2025", "Aditya Sharma, Rahul Verma, Priya Gupta",
      "Initial SRS document creation covering all functional and non-functional requirements for StoryLoom blog platform."]]
)

add_page_break()

# ══════════════════════════════════════════════════════════════════════
# TABLE OF CONTENTS
# ══════════════════════════════════════════════════════════════════════
heading1('Table of Contents')
toc_entries = [
    ("REVISION HISTORY", 0),
    ("1. INTRODUCTION", 0),
    ("   1.1 Purpose", 1),
    ("   1.2 Scope", 1),
    ("   1.3 Definitions, Acronyms, and Abbreviations", 1),
    ("   1.4 References", 1),
    ("   1.5 Overview", 1),
    ("2. GENERAL DESCRIPTION", 0),
    ("   2.1 Product Perspective", 1),
    ("   2.2 Product Functions", 1),
    ("   2.3 User Characteristics", 1),
    ("   2.4 General Constraints", 1),
    ("   2.5 Assumptions and Dependencies", 1),
    ("3. SPECIFIC REQUIREMENTS", 0),
    ("   3.1 External Interface Requirements", 1),
    ("      3.1.1 User Interfaces", 2),
    ("      3.1.2 Hardware Interfaces", 2),
    ("      3.1.3 Software Interfaces", 2),
    ("      3.1.4 Communications Interfaces", 2),
    ("   3.2 Functional Requirements", 1),
    ("      3.2.1 User Registration and Authentication", 2),
    ("      3.2.2 Blog Post Management (Writer)", 2),
    ("      3.2.3 Public Blog Viewing (Reader)", 2),
    ("      3.2.4 Comment System", 2),
    ("      3.2.5 Admin Panel", 2),
    ("      3.2.6 Role-Based Access Control", 2),
    ("   3.5 Non-Functional Requirements", 1),
    ("      3.5.1 Performance", 2),
    ("      3.5.2 Reliability", 2),
    ("      3.5.3 Availability", 2),
    ("      3.5.4 Security", 2),
    ("      3.5.5 Maintainability", 2),
    ("      3.5.6 Portability", 2),
    ("   3.7 Design Constraints", 1),
    ("   3.9 Other Requirements", 1),
    ("4. ANALYSIS MODELS", 0),
    ("   4.1 Data Flow Diagrams (DFD)", 1),
    ("5. GITHUB LINK", 0),
    ("6. DEPLOYED LINK", 0),
    ("7. CLIENT APPROVAL PROOF", 0),
    ("8. CLIENT LOCATION PROOF", 0),
    ("9. TRANSACTION ID PROOF", 0),
    ("10. EMAIL ACKNOWLEDGEMENT", 0),
    ("11. GST No", 0),
    ("A. APPENDICES", 0),
]
for entry, level in toc_entries:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Cm(level * 0.8)
    run = p.add_run(entry)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(11.5 - level * 0.5)
    if level == 0:
        run.bold = True

add_page_break()

# ══════════════════════════════════════════════════════════════════════
# 1. INTRODUCTION
# ══════════════════════════════════════════════════════════════════════
heading1('1. Introduction')
para('This Software Requirements Specification (SRS) document provides a comprehensive and detailed description of the requirements for the StoryLoom blog publishing platform. StoryLoom is a full-stack web application designed to enable writers to create, manage, and publish blog articles, while allowing readers to discover and engage with published content through comments. The platform also provides administrators with moderation tools and user management capabilities.')
para('This document is intended to serve as a reference for the development team, project stakeholders, and evaluators. It describes the product\'s purpose, scope, functional requirements, non-functional requirements, design constraints, and analysis models in compliance with the IEEE 830-1998 recommended practice for SRS documents.')

heading2('1.1 Purpose')
para('The purpose of this SRS document is to define the complete software requirements for the StoryLoom blog publishing platform. This document is intended for the following audiences:')
bullet('Developers: To guide the design, implementation, and testing of the software system.')
bullet('Project Evaluators: To assess the completeness and correctness of the implemented features against stated requirements.')
bullet('Stakeholders / Clients: To understand the scope, features, and constraints of the system.')
bullet('Testers: To derive test cases from the documented functional and non-functional requirements.')
para('This document describes what the system shall do (requirements) and not how it shall be implemented (design), unless design constraints mandate specific implementation approaches.')

heading2('1.2 Scope')
bold_para('Product Name: ', 'StoryLoom – A Laravel-based multi-role blog publishing platform.')

para('StoryLoom will:')
numbered('Provide a public-facing blog website with a homepage, article listing, and individual article pages.')
numbered('Allow users to register and log in with role-based access control (Reader, Writer, Admin).')
numbered('Enable writers to create, edit, save as draft, publish, and delete blog posts through a dedicated writer dashboard.')
numbered('Allow authenticated readers to comment on published articles.')
numbered('Provide an admin panel for platform overview, post management, comment moderation, and user role management.')
numbered('Support MySQL database storage with full migration and seeder support for demo data.')
numbered('Implement a responsive, modern user interface using Tailwind CSS and Blade templating.')

para('StoryLoom will not:')
numbered('Implement rich text or WYSIWYG editing (content is plain text in the current version).')
numbered('Provide file/image upload functionality (featured images are referenced via external URLs).')
numbered('Include search or category-based filtering in the current version.')
numbered('Support API endpoints for external integrations or mobile applications.')

bold_para('Benefits and Goals:')
bullet('Provide a fully functional, role-based blogging platform suitable for real-world editorial workflows.')
bullet('Enable a clear separation of reader, writer, and admin experiences.')
bullet('Deliver a deployable web application with less than 2 seconds page load time under normal usage conditions.')
bullet('Serve as a demonstrable project for academic evaluation of software engineering principles.')

heading2('1.3 Definitions, Acronyms, and Abbreviations')
add_styled_table(doc,
    ["Term", "Definition"],
    [
        ["SRS", "Software Requirements Specification"],
        ["RBAC", "Role-Based Access Control"],
        ["CRUD", "Create, Read, Update, Delete"],
        ["MVC", "Model-View-Controller architectural pattern"],
        ["ORM", "Object-Relational Mapping (Eloquent ORM in Laravel)"],
        ["UI", "User Interface"],
        ["DFD", "Data Flow Diagram"],
        ["Laravel", "PHP web application framework (version 12 used)"],
        ["Blade", "Laravel's built-in templating engine"],
        ["Tailwind CSS", "Utility-first CSS framework (version 4 used)"],
        ["Vite", "Frontend build tool for asset bundling"],
        ["MySQL", "Relational database management system"],
        ["Slug", "A URL-friendly version of a post title (e.g., 'my-first-post')"],
        ["Middleware", "HTTP request filtering mechanism in Laravel"],
        ["Seeder", "Database class that populates tables with sample/demo data"],
    ]
)

heading2('1.4 References')
numbered('IEEE Std 830-1998 – IEEE Recommended Practice for Software Requirements Specifications.')
numbered('Laravel 12 Official Documentation – https://laravel.com/docs/12.x')
numbered('Tailwind CSS v4 Documentation – https://tailwindcss.com/docs')
numbered('Vite Build Tool Documentation – https://vitejs.dev/guide/')
numbered('MySQL 8.0 Reference Manual – https://dev.mysql.com/doc/refman/8.0/en/')
numbered('PHP 8.2 Language Reference – https://www.php.net/manual/en/')
numbered('PHPUnit 11 Documentation – https://phpunit.de/documentation.html')

heading2('1.5 Overview')
para('The remainder of this SRS document is organized as follows:')
bullet('Section 2 – General Description: Provides a high-level overview of the product perspective, product functions, user characteristics, constraints, and assumptions.')
bullet('Section 3 – Specific Requirements: Contains the detailed functional requirements (organized by feature), external interface requirements, non-functional requirements, and design constraints.')
bullet('Section 4 – Analysis Models: Includes Data Flow Diagrams (DFDs) that trace data movement through the system.')
bullet('Sections 5–11: Contain project links, client proofs, and compliance documentation.')
bullet('Appendix A: Provides supplementary information including the database schema and project directory structure.')

add_page_break()

# ══════════════════════════════════════════════════════════════════════
# 2. GENERAL DESCRIPTION
# ══════════════════════════════════════════════════════════════════════
heading1('2. General Description')
para('This section provides a high-level overview of the StoryLoom platform, describing the product context, core functions, intended users, constraints, and foundational assumptions. The details presented here make the specific requirements in Section 3 easier to understand.')

heading2('2.1 Product Perspective')
para('StoryLoom is a self-contained, full-stack web application that operates independently without reliance on external content management systems, third-party APIs, or microservice architectures. It is built as a monolithic Laravel application following the Model-View-Controller (MVC) design pattern.')
para('The product serves as an alternative to heavyweight blogging platforms (such as WordPress) by offering a streamlined, role-driven publishing experience with the following layers:')
bullet('Presentation Layer: Blade templates styled with Tailwind CSS, bundled using Vite.')
bullet('Application Layer: Laravel controllers, middleware, and Eloquent ORM handling business logic.')
bullet('Data Layer: MySQL relational database with normalized schema for users, posts, and comments.')
para('The system is designed for deployment on a standard LAMP/LEMP stack (Linux, Apache/Nginx, MySQL, PHP) or locally using XAMPP on Windows.')

heading2('2.2 Product Functions')
add_styled_table(doc,
    ["Function Category", "Description"],
    [
        ["User Authentication", "Registration with role selection (reader/writer), login, logout, session management with CSRF protection."],
        ["Public Blog Browsing", "Homepage with featured and latest posts, paginated article listing page, individual article detail pages with related posts."],
        ["Writer Dashboard", "CRUD operations for blog posts including title, excerpt, content, featured image URL, status (draft/published), automatic slug generation, and publish date management."],
        ["Reader Commenting", "Authenticated readers can submit comments (5–1200 characters) on published posts; comments are visible by default."],
        ["Admin Dashboard", "Platform overview with statistics (total/published/draft posts, comments, writers), list of recent posts."],
        ["Admin Post Management", "View all posts with pagination, delete any post from the platform."],
        ["Admin Comment Moderation", "View all comments, toggle visibility (visible/hidden), permanently delete comments."],
        ["Admin User Management", "View all users, change user roles between reader, writer, and admin."],
    ]
)

heading2('2.3 User Characteristics')
add_styled_table(doc,
    ["User Role", "Technical Expertise", "Description"],
    [
        ["Reader", "Novice to Intermediate", "General internet users who wish to browse blog articles and engage through comments. They require no technical knowledge beyond basic web browsing."],
        ["Writer", "Intermediate", "Content creators who produce blog articles. Writers should be familiar with basic content management concepts (drafts, publishing)."],
        ["Admin", "Advanced", "Platform administrators responsible for content moderation and user management. Admins should understand editorial workflows and platform governance."],
    ]
)

heading2('2.4 General Constraints')
numbered('Technology Stack Constraint: The system must be built using Laravel 12 (PHP 8.2+), MySQL, Blade templates, and Tailwind CSS v4.')
numbered('Server-Side Rendering: All pages are rendered server-side using Blade. No SPA architecture or client-side JavaScript frameworks.')
numbered('No File Upload: The current version does not support file upload. Featured images are provided as external URLs only.')
numbered('Single-Language Support: The application interface is available in English only.')
numbered('No API Layer: The system does not expose RESTful or GraphQL APIs.')
numbered('Local Development Environment: Primary development and testing is performed on Windows using XAMPP stack.')
numbered('Browser Compatibility: Designed for modern web browsers (Chrome, Firefox, Edge, Safari) with JavaScript enabled.')

heading2('2.5 Assumptions and Dependencies')
numbered('PHP 8.2+ Runtime: The deployment environment has PHP 8.2 or higher installed with required extensions.')
numbered('MySQL 8.0+: MySQL is available and accessible on port 3306 with a database named "storyloom".')
numbered('Composer and NPM: Composer and NPM are installed on the development/deployment machine.')
numbered('Internet Connectivity: Featured images are loaded from external URLs (e.g., Unsplash).')
numbered('XAMPP Availability (Development): For local development, XAMPP is installed and MySQL is running.')
numbered('Modern Browser: Users access the application using a modern web browser with CSS3, HTML5, and JavaScript support.')
numbered('Single Server Deployment: The application is deployed on a single server. Horizontal scaling is not addressed.')

add_page_break()

# ══════════════════════════════════════════════════════════════════════
# 3. SPECIFIC REQUIREMENTS
# ══════════════════════════════════════════════════════════════════════
heading1('3. Specific Requirements')
para('This section contains the detailed requirements that guide the design, implementation, and testing of StoryLoom. Each requirement is uniquely identifiable, traceable, verifiable, and prioritized.')

heading2('3.1 External Interface Requirements')

heading3('3.1.1 User Interfaces')
para('The system provides the following user-facing interfaces, all rendered via Blade templates and styled with Tailwind CSS:')

add_styled_table(doc,
    ["Interface ID", "Interface Name", "Route", "Description"],
    [
        ["UI-01", "Homepage", "/", "Displays the most recent featured post and up to 6 latest published articles."],
        ["UI-02", "Article Listing", "/posts", "Paginated list of all published blog posts (9 per page)."],
        ["UI-03", "Article Detail", "/posts/{slug}", "Full article view with content, author info, featured image, comments, and related posts."],
        ["UI-04", "Login Page", "/login", "Form with email and password fields, 'Remember Me' option."],
        ["UI-05", "Registration Page", "/register", "Form with name, email, role selection, password, and confirmation."],
        ["UI-06", "Writer Dashboard – Post List", "/dashboard/posts", "Paginated list (10/page) of writer's own posts with actions."],
        ["UI-07", "Writer Dashboard – Create Post", "/dashboard/posts/create", "Form for creating a new post."],
        ["UI-08", "Writer Dashboard – Edit Post", "/dashboard/posts/{post}/edit", "Pre-populated form for editing an existing post."],
        ["UI-09", "Admin Dashboard", "/admin", "Platform overview with statistics and recent posts."],
        ["UI-10", "Admin Post Management", "/admin/posts", "Paginated list (12/page) of all posts with delete action."],
        ["UI-11", "Admin Comment Moderation", "/admin/comments", "Paginated list (15/page) with toggle and delete actions."],
        ["UI-12", "Admin User Management", "/admin/users", "Paginated list (15/page) with role change action."],
    ]
)

heading3('3.1.2 Hardware Interfaces')
para('StoryLoom is a web-based application and does not interact directly with any hardware devices. The system requires:')
bullet('A server machine (physical or virtual) capable of running PHP 8.2+, Apache/Nginx, and MySQL 8.0+.')
bullet('Client devices with a modern web browser and internet connectivity.')
bullet('Minimum server specifications: 1 GB RAM, 1 CPU core, 10 GB disk space.')

heading3('3.1.3 Software Interfaces')
add_styled_table(doc,
    ["Software Component", "Version", "Purpose"],
    [
        ["PHP", "≥ 8.2", "Server-side scripting language and runtime environment"],
        ["Laravel Framework", "12.x", "Web application framework providing MVC architecture, routing, ORM, middleware"],
        ["MySQL", "≥ 8.0", "Relational database for persistent data storage"],
        ["Tailwind CSS", "4.x", "Utility-first CSS framework for responsive UI design"],
        ["Vite", "7.x", "Frontend build tool for bundling CSS and JavaScript assets"],
        ["Composer", "≥ 2.x", "PHP dependency manager"],
        ["NPM / Node.js", "≥ 18.x", "JavaScript runtime and package manager for frontend build tools"],
        ["PHPUnit", "11.x", "Testing framework for automated unit and feature tests"],
        ["Apache / Nginx", "Latest stable", "HTTP web server for serving the application"],
    ]
)

heading3('3.1.4 Communications Interfaces')
bullet('HTTP/HTTPS: All client-server communication occurs over HTTP (development) or HTTPS (production).')
bullet('TCP/IP Port 3306: Application communicates with MySQL database server on port 3306.')
bullet('TCP/IP Port 8000: Laravel development server listens on port 8000 by default.')
bullet('CSRF Token Exchange: All form submissions include a CSRF token for protection.')
bullet('Session Cookies: Application uses HTTP cookies for session management stored in MySQL.')

heading2('3.2 Functional Requirements')

# ── FR 3.2.1 ──
heading3('3.2.1 User Registration and Authentication')

heading4('3.2.1.1 Introduction')
para('This feature allows new users to create accounts and existing users to authenticate into the system. The registration process includes role selection, and the login process includes session management with role-based redirection.')

heading4('3.2.1.2 Inputs')
add_styled_table(doc,
    ["Req ID", "Input Field", "Validation Rules", "Context"],
    [
        ["FR-1.1", "Name", "Required, string, max 255 characters", "Registration"],
        ["FR-1.2", "Email", "Required, valid email, max 255 chars, unique in users table", "Registration"],
        ["FR-1.3", "Role", "Required, must be 'reader' or 'writer'", "Registration"],
        ["FR-1.4", "Password", "Required, min 8 chars, confirmed", "Registration"],
        ["FR-1.5", "Email", "Required, valid email format", "Login"],
        ["FR-1.6", "Password", "Required", "Login"],
        ["FR-1.7", "Remember Me", "Optional boolean checkbox", "Login"],
    ]
)

heading4('3.2.1.3 Processing')
bullet('Registration: Validates input, creates user with bcrypt-hashed password (12 rounds), auto-logs in, regenerates session, redirects based on role.')
bullet('Login: Validates credentials via Auth::attempt(), regenerates session, redirects by role (admin → admin dashboard, writer → writer dashboard, reader → homepage).')
bullet('Logout: Invalidates session, regenerates CSRF token, redirects to homepage.')

heading4('3.2.1.4 Outputs')
bullet('Successful registration: redirect with flash message "Your account has been created."')
bullet('Successful login: redirect with flash message "Welcome back!"')
bullet('Successful logout: redirect with flash message "You have been logged out."')

heading4('3.2.1.5 Error Handling')
bullet('Invalid credentials: "These credentials do not match our records." error displayed.')
bullet('Duplicate email: validation error returned.')
bullet('Password mismatch: validation error when password and confirmation do not match.')
bullet('Guest-only routes: authenticated users redirected away via guest middleware.')

# ── FR 3.2.2 ──
heading3('3.2.2 Blog Post Management (Writer Dashboard)')

heading4('3.2.2.1 Introduction')
para('This feature enables writers (and admins) to manage blog posts through a dedicated dashboard. Writers can create, edit, save as draft, publish, and delete posts.')

heading4('3.2.2.2 Inputs')
add_styled_table(doc,
    ["Req ID", "Input Field", "Validation Rules"],
    [
        ["FR-2.1", "Title", "Required, string, max 255 characters"],
        ["FR-2.2", "Excerpt", "Required, string, max 400 characters"],
        ["FR-2.3", "Content", "Required, string, minimum 50 characters"],
        ["FR-2.4", "Featured Image", "Optional, valid URL, max 500 characters"],
        ["FR-2.5", "Status", "Required, must be 'draft' or 'published'"],
    ]
)

heading4('3.2.2.3 Processing')
bullet('Create Post: Validates input, generates unique URL slug from title with collision handling, sets user_id, sets published_at to current timestamp if published.')
bullet('Edit Post: Verifies authorization (owner or admin), validates updated input, regenerates slug if title changed, preserves original published_at.')
bullet('Delete Post: Verifies authorization and permanently deletes the post and all associated comments (cascading delete).')
bullet('List Posts: Writers see only their own posts; admins see all. Paginated at 10 per page.')

heading4('3.2.2.4 Outputs')
bullet('Successful creation: redirect with flash message "Post created successfully."')
bullet('Successful update: redirect with flash message "Post updated successfully."')
bullet('Successful deletion: redirect with flash message "Post deleted."')

heading4('3.2.2.5 Error Handling')
bullet('Unauthorized access (non-owner, non-admin): HTTP 403 Forbidden.')
bullet('Validation errors: returned to the form with error messages.')
bullet('Unauthenticated access: redirect to login page via auth middleware.')
bullet('Non-writer/non-admin role: HTTP 403 via role:writer,admin middleware.')

# ── FR 3.2.3 ──
heading3('3.2.3 Public Blog Viewing')

heading4('3.2.3.1 Introduction')
para('This feature provides the public-facing blog experience for all visitors. It includes the homepage, article listing, and article detail pages.')

heading4('3.2.3.2 Inputs')
add_styled_table(doc,
    ["Req ID", "Input", "Description"],
    [
        ["FR-3.1", "Page number", "Query parameter for pagination on /posts (default: page 1)"],
        ["FR-3.2", "Post slug", "URL parameter identifying a specific post on /posts/{slug}"],
    ]
)

heading4('3.2.3.3 Processing')
bullet('Homepage (/): Queries the most recently published post as featured post, then up to 6 additional published posts.')
bullet('Article Listing (/posts): Queries all published posts, paginated at 9 per page, ordered by publication date descending.')
bullet('Article Detail (/posts/{slug}): Retrieves published post matching slug, eager-loads author, visible comments, and up to 3 related posts.')
bullet('Published Post Criteria: status = "published", published_at is not null, and published_at ≤ current timestamp.')

heading4('3.2.3.4 Outputs')
bullet('Rendered HTML pages displaying post cards (listing) or full content (detail).')
bullet('Pagination controls on the article listing page.')

heading4('3.2.3.5 Error Handling')
bullet('Non-existent or unpublished post slug: HTTP 404 Not Found response.')

# ── FR 3.2.4 ──
heading3('3.2.4 Comment System')

heading4('3.2.4.1 Introduction')
para('This feature allows authenticated users to post comments on published articles. Comments are visible by default and can be moderated by administrators.')

heading4('3.2.4.2 Inputs')
add_styled_table(doc,
    ["Req ID", "Input Field", "Validation Rules"],
    [
        ["FR-4.1", "Comment text", "Required, string, min 5 chars, max 1200 chars"],
        ["FR-4.2", "Post ID", "Route parameter; associated post must be 'published'"],
    ]
)

heading4('3.2.4.3 Processing')
bullet('Verifies the post is published (aborts with 404 if not).')
bullet('Validates comment text against length constraints.')
bullet('Creates a comment record linked to the post and authenticated user, with status "visible".')

heading4('3.2.4.4 Outputs')
bullet('Redirect back to the article page with flash message "Comment added successfully."')
bullet('The new comment appears in the comment section immediately.')

heading4('3.2.4.5 Error Handling')
bullet('Commenting on a non-published post: HTTP 404 response.')
bullet('Unauthenticated user: redirect to login page via auth middleware.')
bullet('Comment too short or too long: validation error returned.')

# ── FR 3.2.5 ──
heading3('3.2.5 Admin Panel')

heading4('3.2.5.1 Introduction')
para('The admin panel provides platform administrators with tools for monitoring, content moderation, and user management.')

heading4('3.2.5.2 Inputs')
add_styled_table(doc,
    ["Req ID", "Input", "Description"],
    [
        ["FR-5.1", "Post ID (for deletion)", "Route parameter identifying the post to delete"],
        ["FR-5.2", "Comment ID (toggle/delete)", "Route parameter identifying the comment to moderate"],
        ["FR-5.3", "User ID (role change)", "Route parameter identifying the user"],
        ["FR-5.4", "New Role", "Required, must be 'admin', 'writer', or 'reader'"],
    ]
)

heading4('3.2.5.3 Processing')
bullet('Dashboard: Aggregates statistics (total posts, published/draft counts, total comments, writer count) and loads 5 most recent posts.')
bullet('Post Management: Lists all posts (paginated at 12) with author details; allows permanent deletion.')
bullet('Comment Moderation: Lists all comments (paginated at 15); allows toggling visibility and permanent deletion.')
bullet('User Management: Lists all users (paginated at 15); allows changing any user\'s role.')

heading4('3.2.5.4 Outputs')
bullet('Dashboard statistics displayed in summary cards.')
bullet('Post deletion: flash message "Post removed by admin."')
bullet('Comment toggle: flash message "Comment status updated."')
bullet('Comment deletion: flash message "Comment deleted."')
bullet('Role update: flash message "User role updated."')

heading4('3.2.5.5 Error Handling')
bullet('Non-admin users: HTTP 403 Forbidden via role:admin middleware.')
bullet('Invalid role value: validation error returned.')
bullet('Non-existent resource: HTTP 404 via Laravel route model binding.')

# ── FR 3.2.6 ──
heading3('3.2.6 Role-Based Access Control (RBAC)')

heading4('3.2.6.1 Introduction')
para('The system implements a custom role-based access control mechanism using Laravel middleware to restrict access to specific routes based on user roles.')

heading4('3.2.6.2 Processing')
add_styled_table(doc,
    ["Req ID", "Route Group", "Middleware", "Allowed Roles"],
    [
        ["FR-6.1", "Public pages (/, /posts, /posts/{slug})", "None (public)", "All users"],
        ["FR-6.2", "Auth pages (/login, /register)", "guest", "Unauthenticated only"],
        ["FR-6.3", "Comment submission", "auth", "All authenticated users"],
        ["FR-6.4", "Writer Dashboard (/dashboard/*)", "auth, role:writer,admin", "Writer and Admin"],
        ["FR-6.5", "Admin Panel (/admin/*)", "auth, role:admin", "Admin only"],
    ]
)

heading4('3.2.6.3 Implementation')
para('The EnsureUserRole middleware accepts a variadic list of role strings. It checks the authenticated user\'s role attribute against the allowed roles using in_array() with strict comparison. If the user\'s role is not in the allowed list, the middleware aborts with HTTP 403.')

# ── Non-Functional Requirements ──
heading2('3.5 Non-Functional Requirements')

heading3('3.5.1 Performance')
add_styled_table(doc,
    ["Req ID", "Requirement", "Metric"],
    [
        ["NFR-1.1", "Page load time for public pages", "≤ 2 seconds under normal load"],
        ["NFR-1.2", "Database query optimization", "Eager loading (with()) used to prevent N+1 query problem"],
        ["NFR-1.3", "Pagination", "All listing pages use Laravel's paginator (9, 10, 12, or 15 per page)"],
        ["NFR-1.4", "Asset bundling", "CSS and JavaScript bundled and minified using Vite for production"],
    ]
)

heading3('3.5.2 Reliability')
add_styled_table(doc,
    ["Req ID", "Requirement", "Description"],
    [
        ["NFR-2.1", "Data integrity", "Foreign key constraints with cascading deletes ensure referential integrity."],
        ["NFR-2.2", "Input validation", "All user inputs validated server-side before processing."],
        ["NFR-2.3", "Unique slug generation", "Collision handling via incrementing suffix ensures unique slugs."],
        ["NFR-2.4", "Automated testing", "PHPUnit test suite available via 'php artisan test'."],
    ]
)

heading3('3.5.3 Availability')
add_styled_table(doc,
    ["Req ID", "Requirement", "Description"],
    [
        ["NFR-3.1", "System availability target", "99% uptime during operational hours."],
        ["NFR-3.2", "Graceful degradation", "If external image URLs are unavailable, system remains functional."],
        ["NFR-3.3", "Database-backed sessions", "Sessions stored in MySQL, persistent across server restarts."],
    ]
)

heading3('3.5.4 Security')
add_styled_table(doc,
    ["Req ID", "Requirement", "Description"],
    [
        ["NFR-4.1", "Password hashing", "Bcrypt with 12 rounds. Plaintext passwords never stored."],
        ["NFR-4.2", "CSRF protection", "All form submissions include CSRF token verified by Laravel."],
        ["NFR-4.3", "Session security", "Sessions regenerated on login, invalidated on logout."],
        ["NFR-4.4", "Role-based authorization", "EnsureUserRole middleware enforces role restrictions with HTTP 403."],
        ["NFR-4.5", "Resource authorization", "Writers can only edit/delete their own posts. Admin bypass explicit."],
        ["NFR-4.6", "Environment secrets", "Sensitive config in .env file excluded from version control."],
        ["NFR-4.7", "Mass assignment protection", "All models use $fillable arrays to whitelist attributes."],
    ]
)

heading3('3.5.5 Maintainability')
add_styled_table(doc,
    ["Req ID", "Requirement", "Description"],
    [
        ["NFR-5.1", "MVC architecture", "Clear separation: Models, Views (Blade), Controllers."],
        ["NFR-5.2", "Modular controllers", "Organized by domain: Public, Auth, Dashboard, Admin namespaces."],
        ["NFR-5.3", "Database migrations", "Schema changes versioned via Laravel migrations."],
        ["NFR-5.4", "Seeder-based demo data", "updateOrCreate() used for idempotent seeding."],
        ["NFR-5.5", "Code standards", "Laravel Pint included for PSR-12 compliant code style."],
    ]
)

heading3('3.5.6 Portability')
add_styled_table(doc,
    ["Req ID", "Requirement", "Description"],
    [
        ["NFR-6.1", "Cross-platform development", "Works on Windows (XAMPP), Linux, or macOS."],
        ["NFR-6.2", "Environment configuration", "All settings externalized to .env file."],
        ["NFR-6.3", "Containerization ready", "Laravel Sail (Docker) included as dev dependency."],
        ["NFR-6.4", "Browser portability", "Compatible with Chrome, Firefox, Edge, Safari."],
    ]
)

heading2('3.7 Design Constraints')
numbered('Framework Constraint: Must use Laravel 12 with built-in routing, middleware, ORM, and templating.')
numbered('Database Constraint: MySQL with InnoDB tables, foreign key constraints, and cascading deletes.')
numbered('Frontend Constraint: Tailwind CSS v4 with Vite build tool and laravel-vite-plugin.')
numbered('PHP Version: Minimum PHP 8.2 required for Laravel 12 compatibility.')
numbered('Authentication Constraint: Manual controller implementation (no Breeze/Jetstream/Fortify starter kit).')
numbered('No JavaScript Frameworks: No React, Vue, Angular, or client-side SPA framework used.')

heading2('3.9 Other Requirements')
numbered('Demo Data: Database seeder creates demo accounts and sample content for immediate testing.')
numbered('Git Safety: .gitignore excludes .env, vendor/, node_modules/, public/build/, logs, and cache files.')
numbered('Setup Documentation: Comprehensive README.md documents installation, demo accounts, routes, and workflows.')
numbered('Idempotent Seeding: updateOrCreate() ensures repeated seeding does not create duplicate records.')

add_page_break()

# ══════════════════════════════════════════════════════════════════════
# 4. ANALYSIS MODELS
# ══════════════════════════════════════════════════════════════════════
heading1('4. Analysis Models')
para('This section presents the analysis models used to visualize data flow, system architecture, and entity relationships within the StoryLoom platform.')

heading2('4.1 Data Flow Diagrams (DFD)')

heading3('4.1.1 Context Diagram (Level 0 DFD)')
para('The context diagram shows the StoryLoom system as a single process interacting with three external entities.')

add_styled_table(doc,
    ["External Entity", "Data Flows IN (to System)", "Data Flows OUT (from System)"],
    [
        ["Reader", "Browse requests, Comment submissions, Registration/Login data", "Published articles, Comment confirmations, Session tokens"],
        ["Writer", "Post data (create/edit/delete), Login credentials", "Post listings, CRUD confirmations, Dashboard views"],
        ["Admin", "Moderation actions (delete/toggle), User role changes", "Platform statistics, Post/Comment/User listings, Confirmations"],
    ]
)
para('Central System: StoryLoom Blog Platform')
para('Data Store: MySQL Database (users, posts, comments, sessions, cache, jobs)')

heading3('4.1.2 Level 1 DFD')
para('The Level 1 DFD decomposes the StoryLoom system into its major processing components.')
add_styled_table(doc,
    ["Process", "Process Name", "Data Input", "Data Output"],
    [
        ["P1", "Authentication Module", "Registration data, Login credentials", "Authenticated session, User record, Role-based redirect"],
        ["P2", "Public Content Display", "Page request, Slug parameter, Pagination", "Homepage view, Article list, Article detail, Related posts"],
        ["P3", "Post Management (Writer)", "Post data (title, excerpt, content, image, status)", "Created/updated/deleted record, Slug, Confirmation"],
        ["P4", "Comment Processing", "Comment text, Post ID, User ID", "Comment record in DB, Confirmation message"],
        ["P5", "Admin Management", "Post/Comment/User IDs, New role value", "Statistics, Moderation actions, Role updates, Confirmations"],
    ]
)

heading3('4.1.3 Entity-Relationship Diagram (ERD)')
para('The following table describes the database entities and their relationships:')
add_styled_table(doc,
    ["Entity", "Key Attributes", "Primary Key", "Relationships"],
    [
        ["users", "id, name, email, role, password, timestamps", "id (auto-increment)", "Has Many → posts, Has Many → comments"],
        ["posts", "id, user_id (FK), title, slug (unique), excerpt, content, featured_image, status, published_at, timestamps", "id (auto-increment)", "Belongs To → users, Has Many → comments"],
        ["comments", "id, post_id (FK), user_id (FK), comment, status, timestamps", "id (auto-increment)", "Belongs To → posts, Belongs To → users"],
        ["sessions", "id, user_id, ip_address, user_agent, payload, last_activity", "id (string)", "Belongs To → users"],
        ["cache", "key, value, expiration", "key (string)", "None"],
        ["jobs", "id, queue, payload, attempts, etc.", "id (auto-increment)", "None (queue infrastructure)"],
    ]
)

heading3('4.1.4 ER Relationship Summary')
para('Relationship Cardinalities:')
bullet('One User can create many Posts (1:N) – cascade delete')
bullet('One User can create many Comments (1:N) – cascade delete')
bullet('One Post can have many Comments (1:N) – cascade delete')

# ER Diagram (text representation)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.LEFT
er_text = """
┌──────────────┐          ┌──────────────┐          ┌──────────────┐
│    USERS     │          │    POSTS     │          │   COMMENTS   │
├──────────────┤          ├──────────────┤          ├──────────────┤
│ PK: id       │──┐      │ PK: id       │──┐      │ PK: id       │
│ name         │  │      │ FK: user_id  │  │      │ FK: post_id  │
│ email        │  │      │ title        │  │      │ FK: user_id  │
│ role         │  ├─1:N──│ slug         │  ├─1:N──│ comment      │
│ password     │  │      │ excerpt      │  │      │ status       │
│ created_at   │  │      │ content      │  │      │ created_at   │
│ updated_at   │  │      │ featured_img │  │      │ updated_at   │
└──────────────┘  │      │ status       │  │      └──────────────┘
                  │      │ published_at │  │
                  │      └──────────────┘  │
                  │                        │
                  └──────── 1:N ───────────┘
"""
run = p.add_run(er_text)
run.font.name = 'Courier New'
run.font.size = Pt(8)

add_page_break()

# ══════════════════════════════════════════════════════════════════════
# 5-11. PROJECT LINKS & PROOFS
# ══════════════════════════════════════════════════════════════════════
heading1('5. GitHub Link')
para('[Insert GitHub repository URL here]')
para('Example: https://github.com/Aditya34as/story_loom')

heading1('6. Deployed Link')
para('[Insert deployed application URL here, if applicable]')
para('Note: StoryLoom is designed for local deployment using XAMPP/LAMP stack. If hosted, provide the live URL.')

heading1('7. Client Approval Proof')
para('[Insert screenshot or document of client approval here]')

heading1('8. Client Location Proof')
para('[Insert proof of client location / meeting location here]')

heading1('9. Transaction ID Proof')
para('[Insert transaction ID or payment proof here, if applicable]')

heading1('10. Email Acknowledgement')
para('[Insert email acknowledgement screenshot or copy here]')

heading1('11. GST No')
para('[Insert GST number here, if applicable]')

add_page_break()

# ══════════════════════════════════════════════════════════════════════
# APPENDICES
# ══════════════════════════════════════════════════════════════════════
heading1('A. Appendices')
para('The following appendices provide supplementary information to support the requirements documented in this SRS.')

heading2('A.1 Appendix 1 – Project Directory Structure')
dir_structure = """blog-platform/
├── app/
│   ├── Http/
│   │   ├── Controllers/
│   │   │   ├── Admin/
│   │   │   │   ├── CommentController.php
│   │   │   │   ├── DashboardController.php
│   │   │   │   ├── PostController.php
│   │   │   │   └── UserController.php
│   │   │   ├── Dashboard/
│   │   │   │   └── PostController.php
│   │   │   ├── AuthController.php
│   │   │   ├── CommentController.php
│   │   │   ├── HomeController.php
│   │   │   └── PublicPostController.php
│   │   └── Middleware/
│   │       └── EnsureUserRole.php
│   ├── Models/
│   │   ├── Comment.php
│   │   ├── Post.php
│   │   └── User.php
│   └── Providers/
├── database/
│   ├── migrations/
│   │   ├── create_users_table.php
│   │   ├── create_cache_table.php
│   │   ├── create_jobs_table.php
│   │   ├── add_role_to_users_table.php
│   │   ├── create_posts_table.php
│   │   └── create_comments_table.php
│   └── seeders/
│       └── DatabaseSeeder.php
├── resources/views/
│   ├── admin/
│   ├── auth/
│   ├── dashboard/
│   ├── layouts/app.blade.php
│   ├── posts/
│   └── home.blade.php
├── routes/
│   ├── web.php
│   └── console.php
├── tests/
├── .env.example
├── composer.json
├── package.json
├── phpunit.xml
├── vite.config.js
└── README.md"""

p = doc.add_paragraph()
run = p.add_run(dir_structure)
run.font.name = 'Courier New'
run.font.size = Pt(9)

heading2('A.2 Appendix 2 – Demo Accounts and Test Data')
para('The following demo accounts are created by the database seeder (php artisan migrate:fresh --seed):')
add_styled_table(doc,
    ["Role", "Name", "Email", "Password"],
    [
        ["Admin", "Platform Admin", "admin@storyloom.test", "password"],
        ["Writer", "Aarav Writer", "writer@storyloom.test", "password"],
        ["Reader", "Riya Reader", "reader@storyloom.test", "password"],
    ]
)

bold_para('Seeded Content:')
bullet('2 published blog posts with featured images (from Unsplash)')
bullet('1 draft blog post (to demonstrate writer workflow)')
bullet('2 comments on published posts (1 from reader, 1 from admin)')

heading2('A.3 Appendix 3 – Complete Route Summary')
add_styled_table(doc,
    ["Method", "URI", "Controller", "Middleware"],
    [
        ["GET", "/", "HomeController", "–"],
        ["GET", "/posts", "PublicPostController@index", "–"],
        ["GET", "/posts/{slug}", "PublicPostController@show", "–"],
        ["GET", "/login", "AuthController@showLogin", "guest"],
        ["POST", "/login", "AuthController@login", "guest"],
        ["GET", "/register", "AuthController@showRegister", "guest"],
        ["POST", "/register", "AuthController@register", "guest"],
        ["POST", "/logout", "AuthController@logout", "auth"],
        ["POST", "/posts/{post}/comments", "CommentController@store", "auth"],
        ["GET", "/dashboard/posts", "Dashboard\\PostController@index", "auth, role:writer,admin"],
        ["GET", "/dashboard/posts/create", "Dashboard\\PostController@create", "auth, role:writer,admin"],
        ["POST", "/dashboard/posts", "Dashboard\\PostController@store", "auth, role:writer,admin"],
        ["GET", "/dashboard/posts/{post}/edit", "Dashboard\\PostController@edit", "auth, role:writer,admin"],
        ["PUT", "/dashboard/posts/{post}", "Dashboard\\PostController@update", "auth, role:writer,admin"],
        ["DELETE", "/dashboard/posts/{post}", "Dashboard\\PostController@destroy", "auth, role:writer,admin"],
        ["GET", "/admin", "Admin\\DashboardController", "auth, role:admin"],
        ["GET", "/admin/posts", "Admin\\PostController@index", "auth, role:admin"],
        ["DELETE", "/admin/posts/{post}", "Admin\\PostController@destroy", "auth, role:admin"],
        ["GET", "/admin/comments", "Admin\\CommentController@index", "auth, role:admin"],
        ["PATCH", "/admin/comments/{comment}/toggle", "Admin\\CommentController@toggle", "auth, role:admin"],
        ["DELETE", "/admin/comments/{comment}", "Admin\\CommentController@destroy", "auth, role:admin"],
        ["GET", "/admin/users", "Admin\\UserController@index", "auth, role:admin"],
        ["PATCH", "/admin/users/{user}/role", "Admin\\UserController@updateRole", "auth, role:admin"],
    ]
)

# ─── Save ───
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "StoryLoom_SRS_Report.docx")
doc.save(output_path)
print(f"✅ Report saved to: {output_path}")
