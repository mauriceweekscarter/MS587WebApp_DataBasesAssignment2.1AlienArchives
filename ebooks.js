// Book content mapped to each button
const books = {
    arrival: "The skies above New Mexico glowed as an unidentified object pierced Earth’s atmosphere...",
    infiltration: "They came silently, blending into humanity. Disguised as neighbors, co-workers, and leaders...",
    galacticwar: "The Zorath Empire declared war on the Alliance after centuries of uneasy peace...",
    abducted: "When Sarah woke up on a cold metal table, she realized she wasn’t on Earth anymore...",
    archives: "The government kept the truth hidden in the Alien Archives: the story behind first contact..."
};

// Function that reads book aloud using Web Speech API
function readBook(bookKey) {
    const utterance = new SpeechSynthesisUtterance(books[bookKey]);
    speechSynthesis.speak(utterance);
}
