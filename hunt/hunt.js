// Shared helpers for the Screenshot Hunt pages.
(function () {
  const cfg = window.HUNT_CONFIG || {};
  const configured = cfg.supabaseUrl && !cfg.supabaseUrl.includes("YOUR-PROJECT");
  const db = configured ? window.supabase.createClient(cfg.supabaseUrl, cfg.supabaseKey) : null;

  function store(kind) {
    return {
      get(k) { try { return window[kind].getItem(k); } catch (e) { return null; } },
      set(k, v) { try { window[kind].setItem(k, v); } catch (e) {} },
      del(k) { try { window[kind].removeItem(k); } catch (e) {} },
    };
  }

  // Newest first. Enough history to number rounds since the last reset.
  async function recentRounds() {
    const { data, error } = await db.from("hunt_rounds").select("*")
      .order("id", { ascending: false }).limit(200);
    if (error) throw error;
    return data;
  }

  // Seconds left in a timed round, or null for untimed rounds.
  function secondsLeft(round) {
    if (!round || round.seconds == null) return null;
    const end = new Date(round.started_at).getTime() + round.seconds * 1000;
    return Math.max(0, Math.ceil((end - Date.now()) / 1000));
  }

  function isOpen(round) {
    if (!round || !round.open) return false;
    const left = secondsLeft(round);
    return left == null || left > 0;
  }

  // "Show QR screen" is stored as a closed round with an empty prompt.
  function isLobby(round) { return !!round && !round.prompt; }
  // "Reset round numbers" is a QR-screen round with seconds = 0.
  function isReset(round) { return isLobby(round) && round.seconds === 0; }

  // The number shown in class: real rounds since the most recent reset. `rounds` is newest first.
  function roundNumber(rounds, round) {
    let n = 0;
    for (const r of rounds.slice(rounds.findIndex((x) => x.id === round.id))) {
      if (isReset(r)) break;
      if (!isLobby(r)) n++;
    }
    return n;
  }

  function imageUrl(path) {
    return db.storage.from("hunt").getPublicUrl(path).data.publicUrl;
  }

  function fmtClock(s) {
    return Math.floor(s / 60) + ":" + String(s % 60).padStart(2, "0");
  }

  function esc(s) {
    return String(s).replace(/[&<>"']/g, (c) =>
      ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);
  }

  function notConfigured(el) {
    el.innerHTML = '<div class="card warn"><b>Not set up yet.</b> Fill in ' +
      "<code>hunt/config.js</code> with your Supabase URL and key (see <code>hunt/README.md</code>).</div>";
  }

  window.Hunt = { db, configured, local: store("localStorage"), session: store("sessionStorage"),
    recentRounds, secondsLeft, isOpen, isLobby, isReset, roundNumber, imageUrl, fmtClock, esc, notConfigured };
})();
