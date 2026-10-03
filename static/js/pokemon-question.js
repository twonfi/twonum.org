const i = setInterval(async () => {
  clearInterval(i);
  const r = await(fetch("/easteregg/"));
  const text = await r.text()
  console.log(text);
}, 1000);
