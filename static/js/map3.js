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

    console.log(typeof(window.mapProjects))

    // Данные для каждого региона
    let regionsData = {};
    regionsData = window.mapProjects;

    let filteredRegionsData = regionsData;

    console.log(filteredRegionsData)

    let tooltipSwiper = null;
    // Обработка наведения на регион
    $('[data-code]').mouseenter(function() {
        const regionCode = $(this).attr('data-code');
        const regionData = filteredRegionsData[regionCode];

        console.log(regionCode)
        console.log(regionData)
        
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
    $('.rf-map.map-3').mouseleave(function() {
        tooltip.classList.remove('visible');
    });

    printCircles();

    function printCircles() {
        const svg = document.querySelector('.rf-map.map-3 svg');
    
        // Удаляем старые круги и тексты, созданные ранее
        svg.querySelectorAll('circle[data-map-circle], text[data-map-count]').forEach(el => el.remove());
    
        for (const regionCode in filteredRegionsData) {
            if (!filteredRegionsData.hasOwnProperty(regionCode)) continue;
    
            const path = svg.querySelector(`[data-code="${regionCode}"]`);
            if (!path) continue;
    
            const bbox = path.getBBox();
            const cx = bbox.x + bbox.width / 2;
            const cy = bbox.y + bbox.height / 2;
    
            const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
            circle.setAttribute('cx', cx);
            circle.setAttribute('cy', cy);
            circle.setAttribute('r', 16);
            circle.setAttribute('fill', 'white');
            circle.setAttribute('data-map-circle', 'true');
            circle.style.pointerEvents = 'none';
            svg.appendChild(circle);
    
            const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
            text.setAttribute('x', cx);
            text.setAttribute('y', cy);
            text.setAttribute('text-anchor', 'middle');
            text.setAttribute('dominant-baseline', 'middle');
            text.setAttribute('fill', 'black');
            text.setAttribute('data-map-count', 'true');
            text.style.transform = 'translateY(1.5px)';
            text.style.fontWeight = 'bold';
            text.style.fontSize = '16px';
            text.style.pointerEvents = 'none';
    
            const projectsCount = filteredRegionsData[regionCode].projects.length;
            text.textContent = projectsCount;
    
            svg.appendChild(text);
        }
    }

    const mapCategories = document.querySelectorAll('.map-subjects-section .filter-panel a'); 

    mapCategories.forEach((category) => {
        category.addEventListener('click', (event) => {
            event.preventDefault(); 

            console.log(category.dataset.categoryName); 
            const categoryName = category.dataset.categoryName;

            let regionsByCategory = null;
            if (categoryName === undefined) {
                regionsByCategory = regionsData;
            } else {
                regionsByCategory = filterRegionsByCategory(categoryName)
            }
            mapCategories.forEach((category) => {
                category.classList.remove('active')
            });
            category.classList.add('active');

            filteredRegionsData = regionsByCategory;

            console.log(filteredRegionsData)

            printCircles()

            updateRegionStyles();
        });
    });

    function filterRegionsByCategory(categoryName) {
        const filtered = {};
    
        for (const regionCode in regionsData) {
            if (!regionsData.hasOwnProperty(regionCode)) continue;
    
            const projects = regionsData[regionCode].projects.filter(project => {
                return project.category === categoryName;
            });
    
            if (projects.length > 0) {
                filtered[regionCode] = { projects };
            }
        }
    
        return filtered;
    }

    function updateRegionStyles(filteredData) {
        let styleTag = document.getElementById('dynamic-region-styles');
    
        if (!styleTag) {
            styleTag = document.createElement('style');
            styleTag.id = 'dynamic-region-styles';
            document.head.appendChild(styleTag);
        }
    
        let cssContent = '';
    
        for (const regionCode in filteredData) {
            cssContent += `
                .rf-map [data-code="${regionCode}"] {
                    fill: var(--color-light-gray);
                    cursor: pointer;
                }
                .rf-map [data-code="${regionCode}"]:hover {
                    fill: rgb(163, 163, 163);
                }
            `;
        }
    
        styleTag.textContent = cssContent;
    }
});

