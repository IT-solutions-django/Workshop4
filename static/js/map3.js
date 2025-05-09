// $(function() {
//     // Создаем тултип
//     const tooltip = document.createElement('div');
//     tooltip.classList.add('map-tooltip-card');
    
//     const tooltipInner = document.createElement('div');
//     tooltipInner.classList.add('tooltip-inner');
    
//     const tooltipImage = document.createElement('img');
//     const tooltipHeading = document.createElement('p');
//     const tooltipSmall = document.createElement('small');
//     const tooltipLabel = document.createElement('label');
    
//     tooltipInner.appendChild(tooltipImage);
//     tooltipInner.appendChild(tooltipLabel);
//     tooltipInner.appendChild(tooltipSmall);
//     tooltipInner.appendChild(tooltipHeading);
    
//     tooltip.appendChild(tooltipInner);
//     document.querySelector('.rf-map.map-3').appendChild(tooltip);

//     // Данные для каждого региона
//     const regionsData = {
//         'RU-SAR':  {
//             image: 'http://91.222.239.153/media/blog/article-card-6.png',
//             title: 'Фьюжн-Квартал',
//             subtitle: 'новый стандарт урбанизма',
//             info: '18 тыс м2 | 2023 г. | Владивосток'
//         },
//         'RU-SA':  {
//             image: 'http://91.222.239.153/media/blog/article-card-6.png',
//             title: 'Фьюжн-Квартал',
//             subtitle: 'новый стандарт урбанизма',
//             info: '18 тыс м2 | 2023 г. | Владивосток'
//         },
//         'RU-KO':  {
//             image: 'http://91.222.239.153/media/blog/article-card-6.png',
//             title: 'Фьюжн-Квартал',
//             subtitle: 'новый стандарт урбанизма',
//             info: '18 тыс м2 | 2023 г. | Владивосток'
//         },
//     };

//     // Обработка наведения на регион
//     $('[data-code]').mouseenter(function() {
//         const regionCode = $(this).attr('data-code');
//         const regionData = regionsData[regionCode];

//         console.log(regionCode)
        
//         if (regionData) {
//             const rect = this.getBoundingClientRect();
            
//             tooltip.style.left = `${rect.right - 80}px`;
//             tooltip.style.top = `${rect.top - 80}px`;
            
//             tooltip.querySelector('img').src = regionData.image;
//             tooltip.querySelector('p').textContent = regionData.title;
//             tooltip.querySelector('small').textContent = regionData.subtitle;
//             tooltip.querySelector('label').textContent = regionData.info;
            
//             tooltip.classList.add('visible');
//         }
//     });

//     // Скрытие тултипа
//     $('[data-code]').mouseleave(function() {
//         tooltip.classList.remove('visible');
//     });
// });



$(function() {
    // Создаем тултип
    const tooltip = document.createElement('div');
    tooltip.classList.add('map-tooltip-card');
    
    const tooltipInner = document.createElement('div');
    tooltipInner.classList.add('tooltip-inner');
    
    // Создаем контейнер для Swiper
    const swiperContainer = document.createElement('div');
    swiperContainer.classList.add('swiper', 'tooltip-swiper');
    
    const swiperWrapper = document.createElement('div');
    swiperWrapper.classList.add('swiper-wrapper');
    
    swiperContainer.appendChild(swiperWrapper);
    tooltipInner.appendChild(swiperContainer);

    // Добавляем кнопки навигации
    const swiperButtonPrev = document.createElement('div');
    swiperButtonPrev.classList.add('tooltip-button-prev');
    
    const swiperButtonNext = document.createElement('div');
    swiperButtonNext.classList.add('tooltip-button-next');
    
    swiperContainer.appendChild(swiperButtonPrev);
    swiperContainer.appendChild(swiperButtonNext);
    
    // Добавляем навигацию Swiper
    const swiperPagination = document.createElement('div');
    swiperPagination.classList.add('swiper-pagination');
    swiperContainer.appendChild(swiperPagination);
    
    tooltip.appendChild(tooltipInner);
    document.querySelector('.rf-map.map-3').appendChild(tooltip);

    // Данные для каждого региона
    const regionsData = {
        'RU-SAR': {
            projects: [
                {
                    image: 'http://91.222.239.153/media/blog/article-card-6.png',
                    title: 'Фьюжн-Квартал',
                    subtitle: 'новый стандарт урбанизма',
                    info: '18 тыс м2 | 2023 г. | Владивосток'
                },
                {
                    image: 'http://91.222.239.153/media/blog/article-card-5.png',
                    title: 'ЖК "Морской"',
                    subtitle: 'современный жилой комплекс',
                    info: '25 тыс м2 | 2024 г. | Владивосток'
                }
            ]
        },
        'RU-SA': {
            projects: [
                {
                    image: 'http://91.222.239.153/media/blog/article-card-6.png',
                    title: 'Проект 1',
                    subtitle: 'описание проекта 1',
                    info: '20 тыс м2 | 2023 г. | Хабаровск'
                },
                {
                    image: 'http://91.222.239.153/media/blog/article-card-5.png',
                    title: 'Проект 2',
                    subtitle: 'описание проекта 2',
                    info: '30 тыс м2 | 2024 г. | Хабаровск'
                }
            ]
        }, 
        'RU-KO': {
            projects: [
                {
                    image: 'http://91.222.239.153/media/blog/article-card-6.png',
                    title: 'Проект 1',
                    subtitle: 'описание проекта 1',
                    info: '20 тыс м2 | 2023 г. | Хабаровск'
                },
                {
                    image: 'http://91.222.239.153/media/blog/article-card-5.png',
                    title: 'Проект 2',
                    subtitle: 'описание проекта 2',
                    info: '30 тыс м2 | 2024 г. | Хабаровск'
                }
            ]
        }
    };

    let tooltipSwiper = null;

    // Обработка наведения на регион
    $('[data-code]').mouseenter(function() {
        const regionCode = $(this).attr('data-code');
        const regionData = regionsData[regionCode];
        
        if (regionData) {
            const rect = this.getBoundingClientRect();
            
            tooltip.style.left = `${rect.right - 80}px`;
            tooltip.style.top = `${rect.top - 80}px`;
            
            // Очищаем предыдущие слайды
            swiperWrapper.innerHTML = '';
            
            // Создаем слайды для каждого проекта
            regionData.projects.forEach(project => {
                const slide = document.createElement('div');
                slide.classList.add('swiper-slide');
                
                slide.innerHTML = `
                    <img src="${project.image}" alt="">
                    <label>${project.info}</label>
                    <small>${project.subtitle}</small>
                    <p>${project.title}</p>
                `;
                
                swiperWrapper.appendChild(slide);
            });

            const projectCounter = document.createElement('div');
            projectCounter.classList.add('project-counter');
            tooltipInner.appendChild(projectCounter);
            projectCounter.textContent = `1/${regionData.projects.length} проектов`;

            if (tooltipSwiper) {
                tooltipSwiper.destroy(true, true);
                tooltipSwiper = null;
            }
            
            // Инициализируем Swiper, если он еще не создан
            if (!tooltipSwiper) {
                tooltipSwiper = new Swiper('.tooltip-swiper', {
                    slidesPerView: 1,
                    spaceBetween: 0,
                    navigation: {
                        nextEl: '.tooltip-button-next',
                        prevEl: '.tooltip-button-prev',
                    },
                    on: {
                        slideChange: function () {
                            // this — это Swiper instance
                            let realIndex = this.realIndex + 1;
                            projectCounter.textContent = `${realIndex}/${regionData.projects.length} проектов`;
                        }
                    },
                    loop: true,
                    autoplay: {
                        delay: 3000,
                        disableOnInteraction: false
                    }
                });
            } else {
                tooltipSwiper.update();
            }
            
            tooltip.classList.add('visible');
        }
    });

    // Скрытие тултипа
    // $('[data-code]').mouseleave(function() {
    //     tooltip.classList.remove('visible');
    // });
});