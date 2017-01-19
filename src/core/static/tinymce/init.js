tinymce.init({
    selector: 'textarea',
    language: 'ru_RU',
    extended_valid_elements : 'script[type|src],iframe[src|style|width|height|scrolling|marginwidth|marginheight|frameborder],div[*],p[*],object[width|height|classid|codebase|embed|param],param[name|value],embed[param|src|type|width|height|flashvars|wmode]',
    verify_html : false,
    plugins: ['link autolink lists preview charmap'],
    menubar: false,
    toolbar: 'undo redo | styleselect | bold italic removeformat | alignleft aligncenter alignright alignjustify | bullist numlist | link charmap preview',

    formats: {
        bold: {block: 'p', inline : 'span', 'classes' : 'text text_bold'},
        italic: {block:'p', inline : 'span', 'classes' : 'text text_italic'},
        alignleft: {selector : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', classes : 'text text_left'},
        aligncenter: {selector : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', classes : 'text text_center'},
        alignright: {selector : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', classes : 'text text_right'},
        alignjustify: {selector : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', classes : 'text text_justify'}
    },
    style_formats: [
        {title: 'Заголовки', items: [
          {title: 'Заголовок 1', block: 'h3', classes: 'title title_l'},
          {title: 'Заголовок 2', block: 'h4', classes: 'title title_m'},
          {title: 'Заголовок 3', block: 'h5', classes: 'title title_s'},
          {title: 'Заголовок 4', block: 'h6', classes: 'title title_xs'}
        ]},
        {title: 'Форматирование текста', items: [
            {title: 'Жирный', block: 'p', inline: 'span', classes: 'text text_bold', icon: 'bold'},
            {title: 'Курсив', block: 'p', inline: 'span', classes: 'text text_italic', icon: 'italic'},
            {title: 'Жирный курсив', block: 'p', inline: 'span', classes: 'text text_bold text_italic', icon: 'italic bold'},
            {title: 'Обычный текст', block: 'p', inline: 'span', classes: 'text', icon: 'italic bold'},
            {title: 'Газетный текст', block: 'p', inline: 'span', classes: 'text text_serif', icon: 'italic bold'}
        ]},
        {title: 'Выравнивание текста', items: [
          {title: 'Слева', classes: 'text text_left', icon: 'alignleft'},
          {title: 'По центру', classes: 'text text_center', icon: 'aligncenter'},
          {title: 'Справа', classes: 'text text_right', icon: 'alignright'},
          {title: 'По ширине', classes: 'text text_justify', icon: 'alignjustify'}
        ]},
        {title: 'Блоки', items: [
          {title: 'Параграф', format: 'p', classes: 'text'}
        ]}
    ],
    content_css: [
        'http://127.0.0.1:8000/static/assets/base.css'
    ]
});