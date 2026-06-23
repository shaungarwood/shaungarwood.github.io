import rss from "@astrojs/rss";
import { getCollection } from "astro:content";
import type { APIContext } from "astro";

export async function GET(context: APIContext) {
	const posts = (await getCollection("posts", (p) => !p.data.draft)).sort(
		(a, b) => b.data.createdAt.valueOf() - a.data.createdAt.valueOf(),
	);

	return rss({
		title: "shaun.",
		description: "runner. hacker. part time hat-wearer.",
		site: context.site!,
		items: posts.map((post) => ({
			title: post.data.title,
			description: post.data.description,
			pubDate: post.data.createdAt,
			link: `/blog/${post.id}/`,
		})),
	});
}
