# crewpvp vanilla mods collection for Fabric client 1.19.4
### Процесс установки:
Первым делом необходимо установить сам клиент по [этой ссылке](https://maven.fabricmc.net/net/fabricmc/fabric-installer/0.11.2/fabric-installer-0.11.2.jar)
Открываем скачанный файл, выбираем раздел 'client', выбираем версию 1.19.4 и указываем директорию куда его стоит установить.
Чаще всего установщик сам определит куда необходимо установить клиент, но вот примерное расположение на разных операционных системах:
MacOS: <Диск с операционной системой>/Users/<Имя пользователя>/Library/Application Support/minecraft/
Linux: /home/<Имя пользователя>/.minecraft/
Windows: <Диск с операционной системой>/Пользователи/<Имя пользователя>/AppData/Roaming/.minecraft/
После установки перейдите в указанную директорию и распакуйте в нее содержимое данного репозитория. Вы можете скачать его [по этой ссылке](https://github.com/crewpvp/minecraft-mods/archive/refs/heads/ver/1.19.4.zip)
В списке версий вашего лаунчера появится новая версия, fabric-loader-0.14.19-1.19.4 (цифры могут отличатся в зависимости от выбранной версии Fabric)

### Решение некоторых проблем
На моем компьютере не запускаются версии выше чем 1.16.5:
- проверьте версию Java. Версия 1.17 требует Java 16 и выше, а начиная с 1.18 - Java 17 и выше. Скачать необходимую вам версию можно [по этой ссылке](https://www.oracle.com/cis/java/technologies/downloads). Не забудьте предварительно удалить старую версию Java, либо укажите необходимую версию в настройках вашего лаунчера.
Обновление версии Java не помогло, версии выше 1.16.5 все так же не запускаются:
- возможно проблема в устаревшем графическом ускорителе вашего ПК, начиная с версии 1.17 Minecraft требует поддержки OpenGL 3.2. Исправить это можно путем установки [данного мода](https://modrinth.com/mod/forcegl20/versions#all-versions). Скачайте необходимую версию и поместите файл в папку 'mods/', в директории Fabric клиента.
Нестабильная работа игры, поддергивания, лаги и прочие проблемы:
- Попробуйте удалить из папки 'mods/', все моды, которые не начинаются с 'optimization-' и 'dependancy-'. К сожалению, если это не поможет - у вас просто устаревший ПК.
Как мне использовать шейдеры с этой сборкой?
- Скачайте и установите [данный мод](https://modrinth.com/mod/iris)
Как мне использовать наборы ресурсов изменяющие небо, которые работают с optifine?
- К существующей сборке добавьте [данный мод](https://modrinth.com/mod/fabricskyboxes-interop)
Раньше я использовал наборы ресурсов, которые делают соединения текстур блоков сглаженными, сейчас это не работает
- Добавьте к существующей сборке [этот](https://modrinth.com/mod/continuity) и [этот мод](https://modrinth.com/mod/indium).
С Optifine мой набор ресурсов заменял некоторые интерфейсы контейнеров, а теперь это не работает
- Установите [данный мод](https://modrinth.com/mod/optigui)
С Optifine мой набор ресурсов заменял модели сущностей, как мне заставить эту функцию работать?
- Добавьте [данный мод](https://www.curseforge.com/minecraft/mc-mods/custom-entity-models-cem) к текущей сборке
Я бы хотел играть с этой сборкой на сервере, который не поддерживает 1.19.4
- Скачайте и установите [данный мод](https://modrinth.com/mod/viafabricplus). Если это вам не помогло, попробуйте один из двух других модов: [ViaFabric](https://modrinth.com/mod/viafabric), [Multiconnect](https://modrinth.com/mod/multiconnect)

### Что из себя представляет сборка
В нее были собраны лучшие моды нацеленные на оптимизацию игры, без критических изменений в самом игровом процессе.
Для работы сборки хватает 1 гб выделенной оперативной памяти.

[Sodium](https://modrinth.com/mod/sodium) - делает большую часть работы по оптимизации, данный мод помимо того, что улучшает игровую производительность, так и исправляет множество графических ошибок.
[Starlight](https://modrinth.com/mod/starlight) - вносит колоссальные изменения в просчет освещения, что дает многократный прирост производительности.
[FerriteCore](https://modrinth.com/mod/ferrite-core) - оптимизирует потребление оперативной памяти, многократно снижая необходимое количество для стабильной работы.
[EntityCulling](https://modrinth.com/mod/entityculling) - заставляет игру перестать обрабатывать сущности (мобов), которые находятся вне видимости игрока.
[FeyTweaks](https://modrinth.com/mod/feytweaks) - оптимизирует отображение лучей от маяков и текст на табличках, скрывая их, когда игрок достаточно далеко.
[ForceCloseLoadingScreen](https://modrinth.com/mod/forcecloseworldloadingscreen) - убирает окно загрузки мира, ускоряет загрузку ресурс паков.
[Krypton](https://modrinth.com/mod/krypton) - оптимизирует сетевой код игры.
[Lithium](https://modrinth.com/mod/lithium) - оптимизирует игровые события (в основном в одиночной игре).
[MemoryLeakFix](https://modrinth.com/mod/memoryleakfix) - исправляет некоторые утечки памяти.
[MoreCulling](https://modrinth.com/mod/moreculling) - заставляет игру перестать обрабатывать блоки, которые находятся вне видимости игрока 
[No Telemetry](https://www.curseforge.com/minecraft/mc-mods/no-telemetry) - отключает сбор данных компание Microsoft о вашем ПК (была заного добавлена в 1.18)
[SmoothBoot](https://modrinth.com/mod/smoothboot-fabric) - позволяет игре запускаться более плавно, распределяя нагрузку при запуске на несколько ядер вашего процессора, вместо одного.
[Exordium](https://modrinth.com/mod/exordium) - позволяет снизить частоту обновления игрового интерфейса, что никак не сказывается на игровом процессе, но дает небольшой выйгрыш по производительности.

Некоторые дополнительные моды для удобства:
[BetterF3](https://modrinth.com/mod/betterf3) - улучшает отображение экрана отладки (F3).
[DontClearChatHistory](https://modrinth.com/mod/dcch) - сохраняет историю отправленных сообщений/команд после выхода с сервера/мира/игры.
[DynamicFPS](https://modrinth.com/mod/dynamic-fps) - снижает громкость игры и частоту кадров в моменты, когда игра свернута
[InGameAccountSwitcher](https://modrinth.com/mod/in-game-account-switcher) - позволяет менять игровой аккаунт не выходя из игры
[MoreChatHistory](https://modrinth.com/mod/morechathistory) - увеличивает лимит истории чата
[NoChatReports](https://modrinth.com/mod/no-chat-reports) - полностью отключает функцию репортов, введенную в 1.19.1
[ScreenshotToClipboard](https://modrinth.com/mod/screenshot-to-clipboard) - загружает сделанный на F2 скриншот сразу в буфер обмена операционной системы
[WI-Zoom](https://www.curseforge.com/minecraft/mc-mods/wi-zoom) - кнопка приближения, аналогичная в OptiFine
[StatusEffectBars](https://modrinth.com/mod/status-effect-bars) - отображает длительность эффекта зелий более наглядно
[SodiumExtra](https://modrinth.com/mod/sodium-extra) - добавляет большее количество настроек графики игры при наличии Sodium
[ReesesSodiumOptions](https://modrinth.com/mod/reeses-sodium-options) - изменяет стандартное меню настроек графики, так, чтобы оно умещалось в любое разрешение игры (необходимо только при наличии SodiumExtra)
[ClothConfig](https://modrinth.com/mod/cloth-config) - добавляет настройки для определенных модов
[WorldEditCUI](https://www.curseforge.com/minecraft/mc-mods/worldeditcui-fabric) - визуально отображает выделение при использовании мода или плагина WorldEdit.

Немножко визуала:
[Visuality](https://modrinth.com/mod/visuality) - добавляет некоторые эффекты на блоки и сущности. Например частиты при дожде на воде, блеск на аметистах, кости при ударе скелета и т.д
[PresenceFootsteps](https://modrinth.com/mod/presence-footsteps) - изменяет звуки шагов в игре на более реалистичные и приятные. К тому же звуки зависят от поверхности на которую наступает сущность.
[ModelFix](https://modrinth.com/mod/modelfix) - убирает визуальный баг с прозрачными линиями между пикселями у предметов.
[NotEnoughAnimations](https://modrinth.com/mod/not-enough-animations) - добавляет новые анимации для игроков, такие как: поднятие/спуск по лестницам, держание карты/предметов в рукеи т.д
[LambDynamicLights](https://modrinth.com/mod/lambdynamiclights) - добавляет динамическое освещение от некоторых сущностей или предметов (когда они надеты/у вас в руке).
[FabricSkyBoxes](https://modrinth.com/mod/fabricskyboxes) - добавляет возможность установки неба (skybox) из ресурс пака с детальной настройкой каждого параметра
[CITResewn](https://www.curseforge.com/minecraft/mc-mods/cit-resewn) - позволяет изменять текстуру предмета исхода из его аттрибутов.

Наборы ресурсов в сборке:
[Faithful 8x8](https://www.curseforge.com/minecraft/texture-packs/f8thful) - стандартный набор ресурсов зашакаленный до 8х8 пикселей. Он был разбит на составляющие, от предметов до интерфейса, может помочь выйграть в производительности, если всё совсем плохо.
[AnimatedTextures](https://www.planetminecraft.com/texture-pack/astraliyte-s-animated-textures) - добавляет анимацию некоторым предметам. Небольшое, но приятное изменение.
[EvenBetterEnchantments](https://www.curseforge.com/minecraft/texture-packs/even-better-enchants) - изменяет книги с зачарованиями на визуально понятные.
Lotzy's sky box - изменяет стандартное небо на новое, в основном только ночное, добавляя к нему полярное сияние, падение комет и т.п
Lotzy's dark gui - изменяет интерфейс на темный вариант, помимо этого изменяет инвентари функциональных блоков на подходящие по стилистике.

 