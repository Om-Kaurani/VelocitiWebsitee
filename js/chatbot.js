/* Velociti AI — Chat Widget for Velociti Studio (rule-based, no API key required) */
(function () {
  const LOGO_SRC = 'assets/images/logo/favicon_icon.png';
  const STORAGE_KEY = 'vs_chat_history';
  const SEEN_KEY = 'vs_chat_launcher_seen';
  const TTS_KEY = 'vs_tts_enabled';
  const BOT_NAME = 'Velociti AI';

  const GREETING_WORDS = ['hi', 'hii', 'hiya', 'hey', 'heya', 'hello', 'yo', 'sup', 'hola', 'howdy'];
  const THANKS_PHRASES = ['thanks', 'thank you', 'thanks a lot', 'ty', 'thankyou', 'appreciate it'];
  const BYE_PHRASES = ['bye', 'goodbye', 'see ya', 'see you', 'cya', 'later', 'good night'];

  // href is relative to the page root, since every page (index/projects/inquiry) sits at the same level.
  const KB = [
    { k: ['service', 'offer', 'what do you do', 'what do you build', 'do you build', 'what kind of'],
      a: "We build custom software, mobile apps, web apps, websites, and AI-powered systems — tailored to what your business actually needs.",
      link: { href: 'index.html#vision', label: 'See our vision' } },
    { k: ['vision', 'philosophy', 'believe in'],
      a: "We're a team of software engineers and designers focused on building things that actually work — no overcomplicated projects, no unnecessary features.",
      link: { href: 'index.html#vision', label: 'Read our vision' } },
    { k: ['communication', 'update', 'progress'],
      a: "We keep you updated in plain, jargon-free language throughout the project, so you always know what's being built, why, and where things stand.",
      link: { href: 'index.html#values', label: 'See how we work' } },
    { k: ['tech', 'technology', 'stack', 'framework', 'tools', 'languages', 'what do you use'],
      a: "We work across Web, Mobile, and AI — we don't force unnecessary technology into a project, we pick the right tools for your specific problem.",
      link: { href: 'index.html#vision', label: 'See our vision' } },
    { k: ['price', 'pricing', 'cost', 'quote', 'estimate', 'budget', 'how much'],
      a: "We use straightforward pricing — no hidden fees or confusing retainers. You get a clear estimate upfront and we stick to it.",
      link: { href: 'inquiry.html', label: 'Request an estimate' } },
    { k: ['small project', 'small business', 'startup', 'too small', 'tight budget'],
      a: "Every project is scoped individually — share your details in the inquiry form and we'll tell you honestly if it's a good fit.",
      link: { href: 'inquiry.html', label: 'Open inquiry form' } },
    { k: ['maintain', 'clean code', 'scalable', 'quality'],
      a: "We write clean, organized code so your product is easy to maintain and scale as your needs grow.",
      link: { href: 'index.html#values', label: 'See how we work' } },
    { k: ['support', 'after delivery', 'maintenance', 'bug'],
      a: "We don't disappear after launch — we make sure everything runs smoothly and provide ongoing support if needed.",
      link: { href: 'index.html#values', label: 'See how we work' } },
    { k: ['ip', 'ownership', 'own the code', 'source code', 'license', 'vendor lock'],
      a: "Once your project is delivered, all source code, design assets, and IP belong entirely to you — no licensing restrictions, no vendor lock-in.",
      link: { href: 'index.html#values', label: 'See how we work' } },
    { k: ['revision', 'change request', 'not happy with', "don't like the design"],
      a: "Revisions are a built-in step in our process — after development, we review the work together and make changes before final delivery.",
      link: { href: 'index.html#process', label: 'View the timeline' } },
    { k: ['process', 'timeline', 'how long', 'how does it work', 'steps', 'stages'],
      a: "Our process: First Meeting (Day 1) → Ideation (Day 2-3) → Planning (Day 4-5) → Development (Week 2-4) → Revisions (Week 5) → Delivery (Week 6).",
      link: { href: 'index.html#process', label: 'View the timeline' } },
    { k: ['team', 'who are you', 'founders', 'developers', 'work here'],
      a: "We're a 6-person team: Nikhil Bhagchandani, Laksh Rewani, Om Kaurani, Yajat Hans, Abhishek Wadhwani, and Harshita Chhabria.",
      link: { href: 'index.html#team', label: 'Meet the team' } },
    { k: ['github', 'code sample', 'see your code'],
      a: "Each team member's GitHub profile is linked on their card in the Team section.",
      link: { href: 'index.html#team', label: 'View team & GitHub links' } },
    { k: ['project', 'work', 'portfolio', 'past work', 'examples', 'built before', 'case stud'],
      a: "Some of our work: Restaurant Owner Portfolio, Nexus Financial Dashboard, Sentinel AI, CargoStream AI, Vitality HealthTrack, and Gesture UI.",
      link: { href: 'projects.html', label: 'View all projects' } },
    { k: ['meeting', 'call', 'schedule', 'book', 'talk to someone'],
      a: "You can schedule a free 30-minute intro meeting directly from our homepage — just pick a date and time.",
      link: { href: 'index.html#contact', label: 'Schedule a meeting' } },
    { k: ['phone number', 'call you', 'your number'],
      a: "We don't list a phone number directly — the fastest ways to reach us are email or booking a free intro call.",
      link: { href: 'index.html#contact', label: 'Go to contact section' } },
    { k: ['contact', 'email', 'reach', 'get in touch'],
      a: "You can email us at velocitistudio@gmail.com, or use the scheduling / estimate options on our homepage.",
      link: { href: 'index.html#contact', label: 'Go to contact section' } },
    { k: ['inquiry', 'form', 'apply', 'start a project', 'hire'],
      a: "Open our inquiry form to share your project details and get a detailed estimate.",
      link: { href: 'inquiry.html', label: 'Open inquiry form' } },
    { k: ['mobile app', 'android', 'ios', 'flutter'],
      a: "Yes — mobile app development is one of our core services, across iOS and Android.",
      link: { href: 'index.html#vision', label: 'Learn more' } },
    { k: ['ai', 'agentic', 'automation', 'machine learning'],
      a: "Yes — we build AI-powered systems and agentic solutions, from predictive dashboards to automation tools.",
      link: { href: 'index.html#work', label: 'See related work' } },
    { k: ['remote', 'location', 'based', 'where are you', 'in person'],
      a: "We're happy to work with clients wherever they're based — book an intro call or email us and we'll figure out what works.",
      link: { href: 'index.html#contact', label: 'Go to contact section' } },
    { k: ['nda', 'confidential', 'confidentiality', 'idea theft', 'steal my idea'],
      a: "That's not something detailed on our site — email us directly and we can discuss confidentiality terms for your project.",
      link: { href: 'index.html#contact', label: 'Go to contact section' } },
    { k: ['refund', 'money back', 'guarantee', 'not satisfied'],
      a: "That's not something detailed on our site — email us directly to discuss this before starting a project.",
      link: { href: 'index.html#contact', label: 'Go to contact section' } },
  ];

  const FALLBACK = "I don't have an answer for that one — email us at velocitistudio@gmail.com or use the inquiry form and we'll get back to you directly.";

  const SUGGESTIONS = [
    { label: 'Our services', q: 'What services do you offer?' },
    { label: 'Pricing', q: 'How much do you charge?' },
    { label: 'Meet the team', q: 'Who is on the team?' },
    { label: 'See our work', q: 'Show me past projects' },
  ];

  function escapeHtml(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
  }

  function htmlToPlainText(html) {
    const div = document.createElement('div');
    div.innerHTML = html;
    return (div.textContent || '').replace(/→/g, '').trim();
  }

  function normalize(m) {
    return m.trim().toLowerCase().replace(/[!.?]+$/, '');
  }

  function matchAnswer(msg) {
    const cleaned = normalize(msg);
    const wordCount = cleaned.split(/\s+/).filter(Boolean).length;
    const firstWord = cleaned.split(/\s+/)[0] || '';

    if (wordCount <= 3) {
      if (GREETING_WORDS.includes(firstWord)) {
        return { html: 'Hello! How can I help you today?' };
      }
      if (THANKS_PHRASES.includes(cleaned)) {
        return { html: "You're welcome! Anything else I can help with?" };
      }
      if (BYE_PHRASES.includes(cleaned)) {
        return { html: 'Thanks for stopping by! Feel free to reach out anytime at velocitistudio@gmail.com.' };
      }
      if (cleaned === 'how are you' || cleaned === 'hows it going') {
        return { html: "I'm doing great, thanks for asking! How can I help you today?" };
      }
      if (['who are you', 'what is your name', "what's your name"].includes(cleaned)) {
        return { html: `I'm ${BOT_NAME} — here to help answer questions about our services, pricing, process, and team.` };
      }
      if (['are you a bot', 'are you real', 'are you human', 'are you ai'].includes(cleaned)) {
        return { html: `I'm ${BOT_NAME}, an automated assistant for Velociti Studio. For anything I can't help with, our team is just an email away.` };
      }
      if (['help', 'what can you do', 'options', 'menu'].includes(cleaned)) {
        return { html: 'I can help with questions about our services, pricing, process, team, past projects, and how to get in touch. What would you like to know?', showSuggestions: true };
      }
    }

    for (const entry of KB) {
      if (entry.k.some(kw => cleaned.includes(kw))) {
        let html = escapeHtml(entry.a);
        if (entry.link) {
          html += ` <a href="${entry.link.href}" class="vs-link">${escapeHtml(entry.link.label)} →</a>`;
        }
        return { html };
      }
    }
    return { html: escapeHtml(FALLBACK) };
  }

  function injectStyles() {
    const css = `
    .vs-chat-btn {
      position: fixed; bottom: 24px; right: 24px; width: 60px; height: 60px;
      border-radius: 50%; background: var(--accent); border: none; cursor: pointer;
      display: flex; align-items: center; justify-content: center;
      box-shadow: 0 4px 20px rgba(255, 100, 31, 0.35);
      z-index: 9999; transition: transform 0.2s ease, background 0.2s ease;
    }
    .vs-chat-btn:hover { background: var(--accent-hover); transform: scale(1.05); }
    .vs-chat-btn svg { width: 26px; height: 26px; }
    .vs-chat-btn.vs-pulse::before {
      content: ''; position: absolute; inset: 0; border-radius: 50%;
      box-shadow: 0 0 0 0 rgba(255, 100, 31, 0.6);
      animation: vs-pulse-ring 2s infinite;
    }
    @keyframes vs-pulse-ring {
      0% { box-shadow: 0 0 0 0 rgba(255, 100, 31, 0.55); }
      70% { box-shadow: 0 0 0 14px rgba(255, 100, 31, 0); }
      100% { box-shadow: 0 0 0 0 rgba(255, 100, 31, 0); }
    }

    .vs-chat-panel {
      position: fixed; bottom: 96px; right: 24px; width: 320px; max-width: calc(100vw - 32px);
      height: 480px; max-height: calc(100vh - 140px);
      background: var(--bg-secondary); border: 1px solid var(--border);
      border-radius: 14px; display: none; flex-direction: column; overflow: hidden;
      box-shadow: 0 12px 40px rgba(0,0,0,0.5); z-index: 9999;
      font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    .vs-chat-panel.open { display: flex; }

    .vs-chat-header {
      background: var(--bg-tertiary); padding: 14px 16px; display: flex;
      align-items: center; justify-content: space-between; border-bottom: 1px solid var(--border);
    }
    .vs-chat-header-title { display: flex; align-items: center; gap: 10px; }
    .vs-chat-header-logo { width: 26px; height: 13px; object-fit: contain; flex-shrink: 0; }
    .vs-chat-header h4 {
      color: var(--text-primary); font-family: var(--font-heading, 'Rajdhani', sans-serif);
      font-size: 1rem; font-weight: 700; margin: 0;
    }
    .vs-chat-header-actions { display: flex; align-items: center; gap: 8px; }
    .vs-chat-header button {
      background: transparent; border: none; color: var(--text-secondary);
      font-size: 1.3rem; cursor: pointer; line-height: 1; padding: 0 2px;
    }
    .vs-chat-header button:hover { color: var(--text-primary); }
    .vs-reset-btn { font-size: 0.7rem !important; text-transform: uppercase; letter-spacing: 0.4px; }
    .vs-tts-btn { font-size: 1rem !important; }
    .vs-tts-btn.vs-active { color: var(--accent-hover); }

    .vs-chat-messages {
      flex: 1; overflow-y: auto; padding: 14px; display: flex; flex-direction: column; gap: 10px;
      scrollbar-width: thin; scrollbar-color: var(--accent) var(--bg-secondary);
    }
    .vs-chat-messages::-webkit-scrollbar { width: 6px; }
    .vs-chat-messages::-webkit-scrollbar-track { background: var(--bg-secondary); }
    .vs-chat-messages::-webkit-scrollbar-thumb { background: var(--accent); border-radius: 4px; }

    .vs-row { display: flex; align-items: flex-end; gap: 8px; max-width: 100%; }
    .vs-row.user { justify-content: flex-end; }
    .vs-avatar {
      width: 24px; height: 24px; border-radius: 50%; background: var(--bg-tertiary);
      border: 1px solid var(--border); object-fit: contain; padding: 4px; flex-shrink: 0;
    }
    .vs-msg { max-width: 78%; padding: 9px 12px; border-radius: 10px; font-size: 0.88rem; line-height: 1.45; word-wrap: break-word; }
    .vs-msg.bot { background: var(--bg-tertiary); color: var(--text-primary); border: 1px solid var(--border); }
    .vs-msg.user { background: var(--accent); color: #fff; }
    .vs-msg a.vs-link { color: var(--accent-hover); font-weight: 600; text-decoration: underline; }

    .vs-typing-dots { display: inline-flex; gap: 4px; align-items: center; padding: 2px 4px; }
    .vs-typing-dots span {
      width: 6px; height: 6px; border-radius: 50%; background: var(--text-secondary);
      animation: vs-bounce 1.2s infinite ease-in-out;
    }
    .vs-typing-dots span:nth-child(2) { animation-delay: 0.15s; }
    .vs-typing-dots span:nth-child(3) { animation-delay: 0.3s; }
    @keyframes vs-bounce { 0%, 60%, 100% { transform: translateY(0); opacity: 0.5; } 30% { transform: translateY(-4px); opacity: 1; } }

    .vs-suggestions { display: flex; flex-wrap: wrap; gap: 6px; padding: 0 14px 12px; }
    .vs-chip {
      background: var(--bg-tertiary); border: 1px solid var(--border); color: var(--text-primary);
      border-radius: 999px; padding: 6px 12px; font-size: 0.78rem; cursor: pointer;
      transition: border-color 0.15s ease, color 0.15s ease;
    }
    .vs-chip:hover { border-color: var(--accent); color: var(--accent-hover); }

    .vs-chat-input-row { display: flex; align-items: center; border-top: 1px solid var(--border); }
    .vs-chat-input-row input {
      flex: 1; background: var(--bg-primary); border: none; color: var(--text-primary);
      padding: 12px 14px; font-size: 0.88rem; font-family: inherit; outline: none;
    }
    .vs-chat-input-row input::placeholder { color: var(--text-secondary); }
    .vs-mic-btn {
      background: transparent; border: none; color: var(--text-secondary); cursor: pointer;
      padding: 0 10px; display: flex; align-items: center; transition: color 0.15s ease;
    }
    .vs-mic-btn:hover { color: var(--accent-hover); }
    .vs-mic-btn.vs-listening { color: #ff4d4d; animation: vs-mic-pulse 1s infinite; }
    @keyframes vs-mic-pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.4; } }
    .vs-chat-input-row button.vs-send-btn {
      background: var(--accent); border: none; color: #fff; padding: 0 18px; height: 46px;
      cursor: pointer; font-weight: 600; font-size: 0.85rem;
    }
    .vs-chat-input-row button.vs-send-btn:hover { background: var(--accent-hover); }

    .vs-footer-link {
      text-align: center; padding: 8px; font-size: 0.72rem; color: var(--text-secondary);
      border-top: 1px solid var(--border); background: var(--bg-tertiary);
    }
    .vs-footer-link a { color: var(--accent-hover); font-weight: 600; }

    @media (max-width: 480px) {
      .vs-chat-panel { right: 16px; bottom: 88px; }
      .vs-chat-btn { right: 16px; bottom: 16px; }
    }
    `;
    const style = document.createElement('style');
    style.textContent = css;
    document.head.appendChild(style);
  }

  function loadHistory() {
    try {
      const raw = sessionStorage.getItem(STORAGE_KEY);
      return raw ? JSON.parse(raw) : [];
    } catch (e) { return []; }
  }

  function saveHistory(history) {
    try { sessionStorage.setItem(STORAGE_KEY, JSON.stringify(history)); } catch (e) { /* ignore */ }
  }

  function renderMessage(container, html, sender) {
    const row = document.createElement('div');
    row.className = 'vs-row ' + sender;

    if (sender === 'bot') {
      const avatar = document.createElement('img');
      avatar.className = 'vs-avatar';
      avatar.src = LOGO_SRC;
      avatar.alt = BOT_NAME;
      row.appendChild(avatar);
    }

    const bubble = document.createElement('div');
    bubble.className = 'vs-msg ' + sender;
    bubble.innerHTML = html;
    row.appendChild(bubble);

    container.appendChild(row);
    container.scrollTop = container.scrollHeight;
    return row;
  }

  function init() {
    injectStyles();

    // --- Speech feature detection ---
    const SpeechRecognitionImpl = window.SpeechRecognition || window.webkitSpeechRecognition;
    const speechRecognitionSupported = !!SpeechRecognitionImpl;
    const speechSynthesisSupported = 'speechSynthesis' in window;

    let ttsEnabled = false;
    try { ttsEnabled = localStorage.getItem(TTS_KEY) === '1'; } catch (e) { /* ignore */ }

    function speak(text) {
      if (!speechSynthesisSupported || !ttsEnabled || !text) return;
      try {
        window.speechSynthesis.cancel();
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.rate = 1;
        utterance.pitch = 1;
        window.speechSynthesis.speak(utterance);
      } catch (e) { /* ignore */ }
    }

    const btn = document.createElement('button');
    btn.className = 'vs-chat-btn';
    btn.setAttribute('aria-label', 'Open ' + BOT_NAME + ' chat');
    btn.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>';

    let seenBefore = false;
    try { seenBefore = localStorage.getItem(SEEN_KEY) === '1'; } catch (e) { /* ignore */ }
    if (!seenBefore) btn.classList.add('vs-pulse');

    const panel = document.createElement('div');
    panel.className = 'vs-chat-panel';
    panel.innerHTML = `
      <div class="vs-chat-header">
        <div class="vs-chat-header-title">
          <img class="vs-chat-header-logo" src="${LOGO_SRC}" alt="${BOT_NAME}">
          <h4>${BOT_NAME}</h4>
        </div>
        <div class="vs-chat-header-actions">
          ${speechSynthesisSupported ? `<button type="button" class="vs-tts-btn" aria-label="Toggle voice replies">🔇</button>` : ''}
          <button type="button" class="vs-reset-btn" aria-label="Reset chat">Reset</button>
          <button type="button" class="vs-close-btn" aria-label="Close chat">&times;</button>
        </div>
      </div>
      <div class="vs-chat-messages"></div>
      <div class="vs-suggestions"></div>
      <div class="vs-chat-input-row">
        <input type="text" placeholder="Ask about our services..." aria-label="Chat message" />
        ${speechRecognitionSupported ? `<button type="button" class="vs-mic-btn" aria-label="Speak your question">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg>
        </button>` : ''}
        <button type="button" class="vs-send-btn">Send</button>
      </div>
      <div class="vs-footer-link">Need a human? <a href="mailto:velocitistudio@gmail.com">Email us directly</a></div>
    `;

    document.body.appendChild(btn);
    document.body.appendChild(panel);

    const messages = panel.querySelector('.vs-chat-messages');
    const suggestionsBox = panel.querySelector('.vs-suggestions');
    const input = panel.querySelector('input');
    const sendBtn = panel.querySelector('.vs-send-btn');
    const closeBtn = panel.querySelector('.vs-close-btn');
    const resetBtn = panel.querySelector('.vs-reset-btn');
    const ttsBtn = panel.querySelector('.vs-tts-btn');
    const micBtn = panel.querySelector('.vs-mic-btn');

    if (ttsBtn) {
      ttsBtn.textContent = ttsEnabled ? '🔊' : '🔇';
      ttsBtn.classList.toggle('vs-active', ttsEnabled);
      ttsBtn.addEventListener('click', () => {
        ttsEnabled = !ttsEnabled;
        try { localStorage.setItem(TTS_KEY, ttsEnabled ? '1' : '0'); } catch (e) { /* ignore */ }
        ttsBtn.textContent = ttsEnabled ? '🔊' : '🔇';
        ttsBtn.classList.toggle('vs-active', ttsEnabled);
        if (!ttsEnabled && speechSynthesisSupported) window.speechSynthesis.cancel();
      });
    }

    let recognition = null;
    let listening = false;
    if (speechRecognitionSupported && micBtn) {
      recognition = new SpeechRecognitionImpl();
      recognition.lang = 'en-US';
      recognition.continuous = false;
      recognition.interimResults = false;

      recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        input.value = transcript;
        send();
      };
      recognition.onerror = () => { listening = false; micBtn.classList.remove('vs-listening'); };
      recognition.onend = () => { listening = false; micBtn.classList.remove('vs-listening'); };

      micBtn.addEventListener('click', () => {
        if (listening) {
          recognition.stop();
          return;
        }
        try {
          recognition.start();
          listening = true;
          micBtn.classList.add('vs-listening');
        } catch (e) { /* already started, ignore */ }
      });
    }

    let history = loadHistory();

    function renderSuggestions() {
      suggestionsBox.innerHTML = '';
      SUGGESTIONS.forEach(s => {
        const chip = document.createElement('button');
        chip.type = 'button';
        chip.className = 'vs-chip';
        chip.textContent = s.label;
        chip.addEventListener('click', () => handleUserMessage(s.q));
        suggestionsBox.appendChild(chip);
      });
    }

    function hideSuggestions() {
      suggestionsBox.innerHTML = '';
    }

    function restoreHistory() {
      messages.innerHTML = '';
      if (history.length === 0) {
        const greetingHtml = `Hi! I'm ${BOT_NAME}. I can help with questions about Velociti Studio — our services, process, pricing, or team. What would you like to know?`;
        renderMessage(messages, greetingHtml, 'bot');
        history.push({ html: greetingHtml, sender: 'bot' });
        saveHistory(history);
        renderSuggestions();
      } else {
        history.forEach(m => renderMessage(messages, m.html, m.sender));
        hideSuggestions();
      }
    }

    let opened = false;
    function open() {
      opened = true;
      panel.classList.add('open');
      restoreHistory();
      input.focus();
      btn.classList.remove('vs-pulse');
      try { localStorage.setItem(SEEN_KEY, '1'); } catch (e) { /* ignore */ }
    }
    function close() {
      opened = false;
      panel.classList.remove('open');
      if (speechSynthesisSupported) window.speechSynthesis.cancel();
      if (recognition && listening) recognition.stop();
    }
    function toggle() { opened ? close() : open(); }

    btn.addEventListener('click', toggle);
    closeBtn.addEventListener('click', close);
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && opened) close(); });

    resetBtn.addEventListener('click', () => {
      history = [];
      saveHistory(history);
      restoreHistory();
    });

    function showTyping() {
      const row = document.createElement('div');
      row.className = 'vs-row bot vs-typing-row';
      row.innerHTML = `<img class="vs-avatar" src="${LOGO_SRC}" alt="${BOT_NAME}">
        <div class="vs-msg bot"><span class="vs-typing-dots"><span></span><span></span><span></span></span></div>`;
      messages.appendChild(row);
      messages.scrollTop = messages.scrollHeight;
      return row;
    }

    function handleUserMessage(text) {
      hideSuggestions();
      renderMessage(messages, escapeHtml(text), 'user');
      history.push({ html: escapeHtml(text), sender: 'user' });
      saveHistory(history);

      const typingRow = showTyping();

      setTimeout(() => {
        typingRow.remove();
        const result = matchAnswer(text);
        renderMessage(messages, result.html, 'bot');
        history.push({ html: result.html, sender: 'bot' });
        saveHistory(history);
        if (result.showSuggestions) renderSuggestions();
        speak(htmlToPlainText(result.html));
      }, 450);
    }

    function send() {
      const text = input.value.trim();
      if (!text) return;
      input.value = '';
      handleUserMessage(text);
    }

    sendBtn.addEventListener('click', send);
    input.addEventListener('keydown', e => { if (e.key === 'Enter') send(); });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
