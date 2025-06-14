export const SITE = {
  website: "https://blog.janakkumarshrestha0.com.np/", // replace this with your deployed domain
  author: "Janak Kr. Shrestha",
  profile: "https://www.janakkumarshrestha0.com.np/",
  desc: "A minimal, responsive and SEO-friendly blog dedicated to DevOps enthusiasts, sharing insights, tutorials, and best practices on automation, CI/CD, containerization, cloud computing, and infrastructure as code. Stay updated with real-world examples, tools, and workflows to streamline development and operations. Perfect for beginners and pros aiming to master modern DevOps culture and technologies.",
  title: "Janak Shrestha",
  ogImage: "astropaper-og.jpg",
  lightAndDarkMode: true,
  postPerIndex: 6,
  postPerPage: 8,
  scheduledPostMargin: 15 * 60 * 1000, // 15 minutes
  showArchives: true,
  showBackButton: true, // show back button in post detail
  editPost: {
    enabled: true,
    text: "Suggest Changes",
    url: "https://github.com/janak0ff/devops-blog/tree/master/",
  },
  dynamicOgImage: true,
  lang: "en", // html lang code. Set this empty and default will be "en"
  timezone: "Asia/Kathmandu", // Default global timezone (IANA format) https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
} as const;
