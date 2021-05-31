let quotesArr = [
  "'If life were predictable it would cease to be life and be without flavor.' -Eleanor Roosevelt",
  '"In the end, it\'s not the years in your life that count. It\'s the life in your years." -Abraham Lincoln',
  '"Life is a succession of lessons which must be lived to be understood." -Ralph Waldo Emerson',
  '"You will face many defeats in life, but never let yourself be defeated." -Maya Angelou',
  '"Never let the fear of striking out keep you from playing the game." -Babe Ruth',
  '"Life is never fair, and perhaps it is a good thing for most of us that it is not." -Oscar Wilde',
  '"The only impossible journey is the one you never begin." -Tony Robbins',
  '"In this life we cannot do great things. We can only do small things with great love." -Mother Teresa',
  '"Only a life lived for others is a life worthwhile." -Albert Einstein',
  '"The purpose of our lives is to be happy." -Dalai Lama',
  '"In three words I can sum up everything I\'ve learned about life: it goes on." -Robert Frost',
  '"Love the life you live. Live the life you love." -Bob Marley',
  '"Life is either a daring adventure or nothing at all." -Helen Keller',
  '"You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose." -Dr. Seuss',
  '"Life is made of ever so many partings welded together." -Charles Dickens',
  "\"Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma -- which is living with the results of other people's thinking.\" -Steve Jobs",
  '"Life is trying things to see if they work." -Ray Bradbury',
  '"Many of life\'s failures are people who did not realize how close they were to success when they gave up." -Thomas A. Edison',
];

const nextWord = (function () {
  let copyArr;
  return function () {
    if (!copyArr || !copyArr) copyArr = quotesArr.slice();
    return copyArr.splice((Math.random() * copyArr.length) | 0, 1);
  };
})();
nextWord();
console.log(nextWord());
