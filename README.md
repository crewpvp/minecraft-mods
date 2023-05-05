# crewpvp vanilla mods collection for Fabric client 1.19.4
### Процесс установки:
Первым делом необходимо установить сам клиент по [этой ссылке](https://maven.fabricmc.net/net/fabricmc/fabric-installer/0.11.2/fabric-installer-0.11.2.jar)</br>
Открываем скачанный файл, выбираем раздел 'client', выбираем версию 1.19.4 и указываем директорию куда его стоит установить.</br>
Чаще всего установщик сам определит куда необходимо установить клиент, но вот примерное расположение на разных операционных системах:</br>
**MacOS**: <Диск с операционной системой>/Users/<Имя пользователя>/Library/Application Support/minecraft/</br>
**Linux**: /home/<Имя пользователя>/.minecraft/</br>
**Windows**: <Диск с операционной системой>/Пользователи/<Имя пользователя>/AppData/Roaming/.minecraft/</br>
После установки перейдите в указанную директорию и распакуйте в нее содержимое данного репозитория. Вы можете скачать его [по этой ссылке](https://github.com/crewpvp/minecraft-mods/archive/refs/heads/ver/1.19.4.zip)</br>
В списке версий вашего лаунчера появится новая версия, fabric-loader-0.14.19-1.19.4 (цифры могут отличатся в зависимости от выбранной версии Fabric)</br>

### Решение некоторых проблем
**На моем компьютере не запускаются версии выше чем 1.16.5:**</br>
\- проверьте версию Java. Версия 1.17 требует Java 16 и выше, а начиная с 1.18 - Java 17 и выше. Скачать необходимую вам версию можно [по этой ссылке](https://www.oracle.com/cis/java/technologies/downloads). Не забудьте предварительно удалить старую версию Java, либо укажите необходимую версию в настройках вашего лаунчера.</br>
**Обновление версии Java не помогло, версии выше 1.16.5 все так же не запускаются:**</br>
\- возможно проблема в устаревшем графическом ускорителе вашего ПК, начиная с версии 1.17 Minecraft требует поддержки OpenGL 3.2. Исправить это можно путем установки [данного мода](https://modrinth.com/mod/forcegl20/versions#all-versions). Скачайте необходимую версию и поместите файл в папку 'mods/', в директории Fabric клиента.</br>
**Нестабильная работа игры, поддергивания, лаги и прочие проблемы:**</br>
\- Попробуйте удалить из папки 'mods/', все моды, которые не начинаются с 'optimization-' и 'dependancy-'. К сожалению, если это не поможет - у вас просто устаревший ПК.</br>
**Как мне использовать шейдеры с этой сборкой?**</br>
\- Скачайте и установите [данный мод](https://modrinth.com/mod/iris)</br>
**Как мне использовать наборы ресурсов изменяющие небо, которые работают с optifine?**</br>
\- К существующей сборке добавьте [данный мод](https://modrinth.com/mod/fabricskyboxes-interop)</br>
**Раньше я использовал наборы ресурсов, которые делают соединения текстур блоков сглаженными, сейчас это не работает**</br>
\- Добавьте к существующей сборке [этот](https://modrinth.com/mod/continuity) и [этот мод](https://modrinth.com/mod/indium).</br>
**С Optifine мой набор ресурсов заменял некоторые интерфейсы контейнеров, а теперь это не работает**</br>
\- Установите [данный мод](https://modrinth.com/mod/optigui)</br>
**С Optifine мой набор ресурсов заменял модели сущностей, как мне заставить эту функцию работать?**</br>
\- Добавьте [данный мод](https://www.curseforge.com/minecraft/mc-mods/custom-entity-models-cem) к текущей сборке</br>
**Я бы хотел играть с этой сборкой на сервере, который не поддерживает 1.19.4**</br>
\- Скачайте и установите [данный мод](https://modrinth.com/mod/viafabricplus). Если это вам не помогло, попробуйте один из двух других модов: [ViaFabric](https://modrinth.com/mod/viafabric), [Multiconnect](https://modrinth.com/mod/multiconnect)</br>
</br>
### Что из себя представляет сборка
В нее были собраны лучшие моды нацеленные на оптимизацию игры, без критических изменений в самом игровом процессе.</br>
Для работы сборки хватает 1 гб выделенной оперативной памяти.</br>
</br>
[Sodium](https://modrinth.com/mod/sodium) - делает большую часть работы по оптимизации, данный мод помимо того, что улучшает игровую производительность, так и исправляет множество графических ошибок.</br>
[Starlight](https://modrinth.com/mod/starlight) - вносит колоссальные изменения в просчет освещения, что дает многократный прирост производительности.</br>
[FerriteCore](https://modrinth.com/mod/ferrite-core) - оптимизирует потребление оперативной памяти, многократно снижая необходимое количество для стабильной работы.</br>
[EntityCulling](https://modrinth.com/mod/entityculling) - заставляет игру перестать обрабатывать сущности (мобов), которые находятся вне видимости игрока.</br>
[FeyTweaks](https://modrinth.com/mod/feytweaks) - оптимизирует отображение лучей от маяков и текст на табличках, скрывая их, когда игрок достаточно далеко.</br>
[ForceCloseLoadingScreen](https://modrinth.com/mod/forcecloseworldloadingscreen) - убирает окно загрузки мира, ускоряет загрузку ресурс паков.</br>
[Krypton](https://modrinth.com/mod/krypton) - оптимизирует сетевой код игры.</br>
[Lithium](https://modrinth.com/mod/lithium) - оптимизирует игровые события (в основном в одиночной игре).</br>
[MemoryLeakFix](https://modrinth.com/mod/memoryleakfix) - исправляет некоторые утечки памяти.</br>
[MoreCulling](https://modrinth.com/mod/moreculling) - заставляет игру перестать обрабатывать блоки, которые находятся вне видимости игрока </br>
[No Telemetry](https://www.curseforge.com/minecraft/mc-mods/no-telemetry) - отключает сбор данных компание Microsoft о вашем ПК (была заного добавлена в 1.18)</br>
[SmoothBoot](https://modrinth.com/mod/smoothboot-fabric) - позволяет игре запускаться более плавно, распределяя нагрузку при запуске на несколько ядер вашего процессора, вместо одного.</br>
[Exordium](https://modrinth.com/mod/exordium) - позволяет снизить частоту обновления игрового интерфейса, что никак не сказывается на игровом процессе, но дает небольшой выйгрыш по производительности.</br>
</br>
Некоторые дополнительные моды для удобства:</br>
[BetterF3](https://modrinth.com/mod/betterf3) - улучшает отображение экрана отладки (F3).</br>
[DontClearChatHistory](https://modrinth.com/mod/dcch) - сохраняет историю отправленных сообщений/команд после выхода с сервера/мира/игры.</br>
[DynamicFPS](https://modrinth.com/mod/dynamic-fps) - снижает громкость игры и частоту кадров в моменты, когда игра свернута</br>
[InGameAccountSwitcher](https://modrinth.com/mod/in-game-account-switcher) - позволяет менять игровой аккаунт не выходя из игры</br>
[MoreChatHistory](https://modrinth.com/mod/morechathistory) - увеличивает лимит истории чата</br>
[NoChatReports](https://modrinth.com/mod/no-chat-reports) - полностью отключает функцию репортов, введенную в 1.19.1</br>
[ScreenshotToClipboard](https://modrinth.com/mod/screenshot-to-clipboard) - загружает сделанный на F2 скриншот сразу в буфер обмена операционной системы</br>
[WI-Zoom](https://www.curseforge.com/minecraft/mc-mods/wi-zoom) - кнопка приближения, аналогичная в OptiFine</br>
[StatusEffectBars](https://modrinth.com/mod/status-effect-bars) - отображает длительность эффекта зелий более наглядно</br>
[SodiumExtra](https://modrinth.com/mod/sodium-extra) - добавляет большее количество настроек графики игры при наличии Sodium</br>
[ReesesSodiumOptions](https://modrinth.com/mod/reeses-sodium-options) - изменяет стандартное меню настроек графики, так, чтобы оно умещалось в любое разрешение игры (необходимо только при наличии SodiumExtra)</br>
[ClothConfig](https://modrinth.com/mod/cloth-config) - добавляет настройки для определенных модов</br>
[WorldEditCUI](https://www.curseforge.com/minecraft/mc-mods/worldeditcui-fabric) - визуально отображает выделение при использовании мода или плагина WorldEdit.</br>
</br>
Немножко визуала:</br>
[Visuality](https://modrinth.com/mod/visuality) - добавляет некоторые эффекты на блоки и сущности. Например частиты при дожде на воде, блеск на аметистах, кости при ударе скелета и т.д</br>
[PresenceFootsteps](https://modrinth.com/mod/presence-footsteps) - изменяет звуки шагов в игре на более реалистичные и приятные. К тому же звуки зависят от поверхности на которую наступает сущность.</br>
[ModelFix](https://modrinth.com/mod/modelfix) - убирает визуальный баг с прозрачными линиями между пикселями у предметов.</br>
[NotEnoughAnimations](https://modrinth.com/mod/not-enough-animations) - добавляет новые анимации для игроков, такие как: поднятие/спуск по лестницам, держание карты/предметов в рукеи т.д</br>
[LambDynamicLights](https://modrinth.com/mod/lambdynamiclights) - добавляет динамическое освещение от некоторых сущностей или предметов (когда они надеты/у вас в руке).</br>
[FabricSkyBoxes](https://modrinth.com/mod/fabricskyboxes) - добавляет возможность установки неба (skybox) из ресурс пака с детальной настройкой каждого параметра</br>
[CITResewn](https://www.curseforge.com/minecraft/mc-mods/cit-resewn) - позволяет изменять текстуру предмета исхода из его аттрибутов.</br>
</br>
Наборы ресурсов в сборке:</br>
[Faithful 8x8](https://www.curseforge.com/minecraft/texture-packs/f8thful) - стандартный набор ресурсов зашакаленный до 8х8 пикселей. Он был разбит на составляющие, от предметов до интерфейса, может помочь выйграть в производительности, если всё совсем плохо.</br>
[AnimatedTextures](https://www.planetminecraft.com/texture-pack/astraliyte-s-animated-textures) - добавляет анимацию некоторым предметам. Небольшое, но приятное изменение.</br>
[EvenBetterEnchantments](https://www.curseforge.com/minecraft/texture-packs/even-better-enchants) - изменяет книги с зачарованиями на визуально понятные.</br>
Lotzy's sky box - изменяет стандартное небо на новое, в основном только ночное, добавляя к нему полярное сияние, падение комет и т.п</br>
Lotzy's dark gui - изменяет интерфейс на темный вариант, помимо этого изменяет инвентари функциональных блоков на подходящие по стилистике.</br>

 