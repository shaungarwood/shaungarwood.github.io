import mdx from "@astrojs/mdx";
import sitemap from "@astrojs/sitemap";
import { defineConfig } from "astro/config";
import expressiveCode from "astro-expressive-code";
import spectre from "./package/src";
import { spectreDark } from "./src/ec-theme";

// https://astro.build/config
const config = defineConfig({
	site: "https://shaungarwood.com",
	output: "static",
	integrations: [
		expressiveCode({
			themes: [spectreDark],
		}),
		mdx(),
		sitemap(),
		spectre({
			name: "shaun.",
			openGraph: {
				home: {
					title: "shaun.",
					description: "runner. hacker. part time hat-wearer.",
				},
				blog: {
					title: "Blog",
					description: "Findings, notes, hacks, ideas, rants, raves, musings, and thoughts.",
				},
				projects: {
					title: "Projects",
				},
			},
		}),
	],
});

export default config;
