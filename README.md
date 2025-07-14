# static-site-generator
Static site generator in python. Boot.dev project.

# How to use:
Simply fill the "content" folder with markdown files you wish to be converted to raw HTML (the root index.md file will be the home page, for other pages create a new directory as well as nested directories with an index.md file within).
The Template can be edited but all content will fall under the {{ Content }} section.
The CSS Styling is also available to edit within the "static" directory.
Any additional files that are needed (Images etc.) simply place in the "static" folder and use links for them relative to the "static" directory in your pages.
Once all markdown content and static content is ready, simply run main.sh to generate your site and run it locally (default port is 8888, this can be changed in main.sh file) or run build.sh to generate your site using the optional base filepath argument (default is "static-site-generator")
