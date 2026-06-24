const badge = document.getElementById("gpg-badge") as HTMLElement | null;
if (!badge) throw new Error("no badge");

const slug = badge.dataset.slug!;
const btn = document.getElementById("verify-btn") as HTMLButtonElement;
const result = document.getElementById("verify-result") as HTMLElement;

btn.addEventListener("click", async () => {
  btn.disabled = true;
  btn.textContent = "Verifying…";
  result.className = "verify-result";
  result.textContent = "";

  try {
    const { readKey, readSignature, createMessage, verify } = await import("openpgp");

    const [publicKeyArmored, signatureArmored, messageText] = await Promise.all([
      fetch("/pgp-key.asc").then((r) => r.text()),
      fetch(`/signatures/${slug}.asc`).then((r) => r.text()),
      fetch(`/source/${slug}`).then((r) => r.text()),
    ]);

    const publicKey = await readKey({ armoredKey: publicKeyArmored });
    const signature = await readSignature({ armoredSignature: signatureArmored });
    const message = await createMessage({ text: messageText });

    const verification = await verify({ message, signature, verificationKeys: publicKey });
    await verification.signatures[0].verified; // throws if bad

    result.className = "verify-result verify-ok";
    result.textContent = "✓ Valid signature — verified by your browser";
  } catch (e) {
    result.className = "verify-result verify-fail";
    result.textContent = `✗ Verification failed — ${e instanceof Error ? e.message : "unknown error"}`;
  } finally {
    btn.disabled = false;
    btn.textContent = "Verify in browser";
  }
});
