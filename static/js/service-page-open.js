const header = document.querySelector('header'); 
const main = document.querySelector('main'); 
const mainBg = document.querySelector('.main-bg');

runHomePreloader()

function generateTextSteps(finalText) {
    const steps = [];
    let currentText = '';
    
    // Разбиваем текст на слова
    const words = finalText.split(' ');
    
    // Генерируем промежуточные состояния
    for (let i = 0; i < words.length; i++) {
        // Для коротких слов (до 4 букв) добавляем только полное слово
        if (words[i].length <= 4) {
            currentText = words.slice(0, i + 1).join(' ');
            steps.push(currentText);
            continue;
        }
        
        // Для длинных слов добавляем промежуточные состояния
        const word = words[i];
        const parts = [];
        
        // Разбиваем слово на логические части
        if (word.length > 4) {
            // Начинаем с первых трёх букв
            parts.push(word.substring(0, 3));
            
            // Добавляем промежуточные части
            for (let j = 4; j < word.length; j += 2) {
                parts.push(word.substring(0, j));
            }
            
            // Добавляем полное слово
            parts.push(word);
        }
        
        // Формируем промежуточные состояния
        for (const part of parts) {
            currentText = words.slice(0, i).join(' ') + ' ' + part;
            steps.push(currentText);
        }
    }
    
    return steps;
}

function runHomePreloader() {
    let cont = $('h1'),
        p = 0;
    text = 'Fands.Agency';
    cont.html("");

    randomRange = 120;

    let fixedInterval = 40;

    function printHeading(onPrintComplete) {
        let timeout = fixedInterval;
        let currentIndex = 0;
        let texts = generateTextSteps(window.serviceName || 'Проектирование конструктивных решений');

        function runNextStep() {
            if (currentIndex >= texts.length) {
                setTimeout(onPrintComplete, 30);
                return;
            }

            cont.text(texts[currentIndex]);
            currentIndex++;

            setTimeout(runNextStep, fixedInterval);
        }

        runNextStep();
    }

    function onPrintComplete() {
        console.log('onPrintComplete');
        document.querySelector('.preloader-divider')?.classList.add('active');

        setTimeout(() => {
            header.classList.add('active');
            main.classList.add('active');
            body.classList.add('active');

            setTimeout(() => {
                body.classList.add('scrollable');
                document.querySelector('.company-main-block p').style.opacity = 1;
                mainBg.classList.add('active');
                switchTexts();
            }, 700);
        }, 100);
    }
    setTimeout(() => printHeading(onPrintComplete), 150);
}