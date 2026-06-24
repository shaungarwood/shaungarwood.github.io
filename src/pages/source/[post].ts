import type { APIRoute, GetStaticPaths } from "astro";
import { getCollection } from "astro:content";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";

export const getStaticPaths = (async () => {
	const posts = await getCollection("posts", (post) => post.data.draft !== true);
	return posts.map((post) => ({ params: { post: post.id } }));
}) satisfies GetStaticPaths;

export const GET: APIRoute = async ({ params }) => {
	let content: string;
	for (const ext of ["mdx", "md"]) {
		try {
			content = await readFile(
				resolve(`src/content/posts/${params.post}.${ext}`),
				"utf-8",
			);
			return new Response(content, {
				headers: { "Content-Type": "text/plain; charset=utf-8" },
			});
		} catch {}
	}
	return new Response("Not found", { status: 404 });
};
