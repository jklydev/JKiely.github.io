import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context) {
  const posts = await getCollection('blog');

  return rss({
    title: 'JKLY',
    description: 'Updates and writing from JKLY, now powered by Astro.',
    site: context.site ?? 'https://www.jkly.io',
    items: posts
      .filter((post) => !post.data.draft)
      .map((post) => ({
        title: post.data.title,
        description: post.data.description,
        link: `/blog/${post.slug}/`,
        pubDate: post.data.publishDate
      }))
  });
}
