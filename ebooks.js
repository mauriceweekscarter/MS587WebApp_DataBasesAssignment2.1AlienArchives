const ebooks = [
    { title: "The Arrival: First Contact", content: "The skies above New Mexico glowed as an unidentified object pierced Earth's atmosphere. A lone figure emerged, signaling the beginning of Earth's first encounter with alien life." },
    { title: "Alien Infiltration: Among Us", content: "They came silently, blending into humanity. Disguised as neighbors, coworkers, and leaders, the aliens observed and manipulated human society from within." },
    { title: "Galactic War: The Zorath Conflict", content: "The Zorath Empire declared war on the Alliance after centuries of uneasy peace. Massive starships clashed across galaxies as alliances shifted and planets struggled to survive." },
    { title: "Abducted: The Human Experiment", content: "When Sarah woke up on a cold metal table, she realized she wasn’t on Earth anymore. The aliens had been studying humans for generations, seeking to unlock the secrets of their DNA." },
    { title: "The Alien Archives: Hidden Truth", content: "Deep within government vaults lie the Alien Archives — classified files documenting decades of extraterrestrial encounters, abductions, and covert operations." }
];
const bookList = document.getElementById('book-list');
ebooks.forEach((book, index) => {
    const btn = document.createElement('button');
    btn.innerText = book.title;
    btn.onclick = () => showBook(index);
    bookList.appendChild(btn);
});
function showBook(index) {
    document.getElementById('reader-section').classList.remove('hidden');
    document.getElementById('book-title').innerText = ebooks[index].title;
    document.getElementById('book-content').innerText = ebooks[index].content;
    currentBook = ebooks[index];
}
let currentBook = null;
function readAloud() {
    if (!currentBook) return;
    const utterance = new SpeechSynthesisUtterance(currentBook.content);
    utterance.voice = speechSynthesis.getVoices().find(voice => voice.lang.startsWith('en')) || null;
    speechSynthesis.speak(utterance);
}
