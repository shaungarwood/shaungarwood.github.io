import rss from "@astrojs/rss";
import { getCollection } from "astro:content";
import type { APIContext } from "astro";
import MarkdownIt from "markdown-it";
import sanitizeHtml from "sanitize-html";

const parser = new MarkdownIt();

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
			pubDate: post.data.createdAt,
			link: `/blog/${post.id}/`,
			content: sanitizeHtml(parser.render(post.body ?? ""), {
				allowedTags: sanitizeHtml.defaults.allowedTags.concat(["img"]),
			}),
		})),
	});
}
