import rss from "@astrojs/rss";
import { getCollection } from "astro:content";
import type { APIContext } from "astro";

export async function GET(context: APIContext) {
	const notes = (await getCollection("notes")).sort((a, b) => {
		const dateDiff = b.data.date.valueOf() - a.data.date.valueOf();
		if (dateDiff !== 0) return dateDiff;
		return b.id.localeCompare(a.id);
	});

	return rss({
		title: "shaun. — notes",
		description: "Short thoughts from Shaun.",
		site: context.site!,
		items: notes.map((note) => ({
			title: note.data.date.toLocaleDateString("en-US", {
				year: "numeric",
				month: "long",
				day: "numeric",
			}),
			description: (note.body ?? "").replace(/^---[\s\S]*?---\n*/m, "").trim().slice(0, 280),
			pubDate: note.data.date,
			link: `/notes/#${note.id}`,
		})),
	});
}
