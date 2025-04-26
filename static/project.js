document.addEventListener('DOMContentLoaded', () => {
    const track = document.querySelector('.carousel-track');
    if (!track) return;
  
    const slides = Array.from(track.children);
    const prevBtn = document.querySelector('.carousel-button.prev');
    const nextBtn = document.querySelector('.carousel-button.next');
    const slideWidth = slides[0].getBoundingClientRect().width;
  
    // position slides side by side
    slides.forEach((slide, idx) => {
      slide.style.left = (slideWidth * idx) + 'px';
    });
  
    const moveTo = (targetIdx) => {
      track.style.transform = 'translateX(-' + (slideWidth * targetIdx) + 'px)';
      slides.forEach((s, i) => {
        s.classList.toggle('shadowed', i < slides.length - 1 && i !== targetIdx);
      });
      currentIndex = targetIdx;
    };
  
    let currentIndex = 0;
    prevBtn.addEventListener('click', () => {
      const newIndex = (currentIndex - 1 + slides.length) % slides.length;
      moveTo(newIndex);
    });
    nextBtn.addEventListener('click', () => {
      const newIndex = (currentIndex + 1) % slides.length;
      moveTo(newIndex);
    });
  });
  