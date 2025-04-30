// File: static/project.js

document.addEventListener('DOMContentLoaded', () => {
  const track = document.querySelector('.carousel-track');
  if (!track) return;

  const slides = Array.from(track.children);
  const prevBtn = document.querySelector('.carousel-button.prev');
  const nextBtn = document.querySelector('.carousel-button.next');
  let currentIndex = 0;

  // Reposition the track to the given index, recalculating width each time
  const moveTo = (targetIdx) => {
    const slideWidth = slides[0].getBoundingClientRect().width;
    track.style.transform = `translateX(-${slideWidth * targetIdx}px)`;
    slides.forEach((s, i) => {
      s.classList.toggle('shadowed', i < slides.length - 1 && i !== targetIdx);
    });
    currentIndex = targetIdx;
  };

  // Initial positioning
  moveTo(0);

  prevBtn.addEventListener('click', () => {
    const newIndex = (currentIndex - 1 + slides.length) % slides.length;
    moveTo(newIndex);
  });

  nextBtn.addEventListener('click', () => {
    const newIndex = (currentIndex + 1) % slides.length;
    moveTo(newIndex);
  });

  // If the window resizes, re-center on the current slide
  window.addEventListener('resize', () => {
    moveTo(currentIndex);
  });
});
