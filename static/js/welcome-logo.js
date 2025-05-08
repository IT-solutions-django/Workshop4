document.addEventListener('DOMContentLoaded', () => {

    const bg = document.querySelector('.bg');
    const container = document.querySelector('.container');
    
    // Регистрируем плагин ScrollTrigger
    gsap.registerPlugin(ScrollTrigger);
    
    // Создаем анимацию
    gsap.to(bg, {
        y: () => -(document.body.scrollHeight - window.innerHeight),
        ease: "none",
        scrollTrigger: {
            trigger: "body",
            start: "top top",
            end: "bottom bottom",
            scrub: 1,
            invalidateOnRefresh: true
        }
    });
});
