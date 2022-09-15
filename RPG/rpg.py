class Personagem:
    def __init__(self,nome,raça,classe):
        self.nome = nome
        self.raça = raça
        self.classe = classe
    def atributos(self,strenght,intelligence,sabedoria,skill,charisma,resistance):
        self.strenght = strenght
        self.intelligence = intelligence
        self.sabedoria = sabedoria
        self.skill = skill
        self.charisma = charisma
        self.resistance = resistance
    def mostrarAtri(self):
        print(f'Atributos:\n•Força: {self.strenght}\n•Inteligencia: {self.intelligence}\n•Sabedoria: {self.sabedoria}\n•Destreza: {self.skill}\n•Carisma: {self.charisma}\n•Resistencia: {self.resistance}\n')
    def skillsraça (self,sraça):
        sraça = self.raça
        match sraça:
            case 'Anões':
                self.strenght += 2
                self.resistance += 2
                self.descRaça = ('Esculpidos nas fundações rochosas do universo, os anões suportaram uma era de servidão aos gigantes antes de conquistar sua liberdade.\n•  É robusto, severo e poderoso como uma rocha.\n•  Trazer glória para os seus ancestrais ou servir como o braço direito de seu deus.\n•  Ser capaz de suportar os piores castigos.\n•  Uma raça que privilegia as classes clérigo e guerreiro.')
            case 'Draconatos':
                self.strenght += 2
                self.charisma += 1
                self.descRaça = ('Descendentes de dragões, como seus nomes demonstram, os draconatos andam orgulhosamente pelo mundo que os saúda com um temor incompreensível.\n•  Moldados por deuses dracônicos ou pelos próprios dragões.\n•  Draconatos originalmente nasceram de ovos de dragão como uma raça única.\n•  Combina os melhores atributos de dragões e humanos.')
            case 'Elfos':
                self.intelligence += 1
                self.skill += 2
                self.charisma += 2
                self.descRaça = ('Elfos são um povo mágico de graça sobrenatural, vivendo no mundo sem pertencer inteiramente à ele.\n•  Eles vivem em lugares de beleza etérea, no meio de antigas florestas ou em torres prateadas brilhando com luz feérica, onde uma música suave ecoa através do ar e fragrâncias suaves flutuam na brisa.\n•  Elfos amam a natureza e a magia, a arte e o estudo, a música e a poesia, e as coisas boas do mundo.')
            case 'Gnomos':
                self.intelligence += 2
                self.skill += 1
                self.resistance += 1
                self.descRaça = ('Um zumbido constante de atividades permeia a vizinhança onde os gnomos formam suas comunidades privadas.\n•  Barulhos estrondosos pontuam o zumbido: um tilintar de engrenagens moendo aqui, uma pequena explosão ali, um grito de surpresa ou comemoração e, principalmente, muitas gargalhadas.\n•  Gnomos regozijam a vida, apreciando cada momento de invento, exploração, investigação, criação e brincadeira.\n•  A energia e entusiasmo dos gnomos pela vida brilha em cada pedacinho do seu pequeno corpo.')
            case 'Halflings':
                self.skill += 2
                self.charisma += 1
                self.resistance += 1
                self.descRaça = ('Halflings são um povo afável e alegre. Eles apreciam os laços de família e amizade, bem como o conforto do lar e da casa, nutrindo poucos sonhos de ouro e glória.\n•  Mesmo os aventureiros que existem entre eles normalmente aventuram-se no mundo por razões de comunidade, amizade, desejo de viajar ou curiosidade.\n•  Eles amam descobrir coisas novas, até mesmo as mais simples, tais como uma comida exótica ou um estilo estranho de vestuário. Halflings são facilmente movidos pela piedade e detestam ver qualquer ser vivo sofrer.\n•  Eles são generosos, partilhando alegremente o que eles possuem, mesmo em épocas de vacas magras.')
            case 'Humanos':
                self.strenght += 1
                self.intelligence += 1
                self.sabedoria += 1
                self.skill += 1
                self.charisma += 1
                self.resistance += 1
                self.descRaça = ('Os humanos são os mais adaptáveis, flexíveis e ambiciosos entre todas as raças comuns.\n•  Eles têm amplos e distintos gostos, moralidades e hábitos nas muitas diferentes regiões onde eles se instalaram.\n•  Quando se estabelecem em um lugar, eles permanecem: eles constroem cidades que duram por eras, e grandes reinos que podem persistir por longos séculos.\n•  Um único humano pode ter uma vida relativamente curta, mas uma nação ou cultura humana preserva tradições com origens muito além do alcance da memória de qualquer um dos humanos.')
            case 'Kor':
                self.sabedoria += 1
                self.skill += 2
                self.descRaça = ('Os kor se adaptam a qualquer ambiente, suas tribos normalmente se localizam em regiões de dificil acesso.\n•  Eles acham que não a necessidade de alterar o ambiente para poder criar um lar.\n•  Kors tratam o solo como um tesouro, e normalmente kors estudam a arte da geomancia ( magia de controlar a terra ).')
            case 'Meio-Orc':
                self.strenght += 2
                self.resistance += 1
                self.descRaça = ('Os meio-orcs, apesar do seu sangue humano tem moderar o impacto da sua herança Orc, alguns Meio-Orcs ouvem os sussurros de Gruumsh em seus sonhos, influenciando-os a liberar a fúria que fervilha dentro deles.\n•  Meio-orcs não são maus por natureza, mas o mal espreita dentro deles, quer eles o abracem ou se rebelem contra ele.\n•  Além da fúria de Gruumsh, meio-orcs sentem poderosas emoções.\n•  A fúria não apenas acelera seu pulso, mas faz seus corpos arder.')
            case 'Replicante':
                self.skill += 1
                self.charisma += 1
                self.descRaça = ('Os replicantes são capazes de transmutar seu corpo, assumindo uma segunda persona em um piscar de olhos.\n•  Embora eles não consigam alterar sua forma de maneira radical, um replicante é capaz de alterar sua aparência de forma livre.\n•  Replicantes usam sua capacidade de adotar a forma de outras criaturas para se tornarem espiões e criminosos consumados.')
            case 'Tieflings':
                self.intelligence += 1
                self.charisma += 2
                self.descRaça = ('Os tieflings são definidos como os herdeiros de uma linhagem infernal, de um império decaído.\n•  Eles vivem nas sombras e não temem a escuridão e as trevas.\n•  Eles são descendentes de humanos nobres que barganhavam com poderes sombrios, que há muito tempo, ergueram um império que subjugou metade do mundo.\n•  Eles vivem dentro dos territórios e cidades humanos.')
            case 'Tritão':
                self.strenght += 1
                self.charisma += 1
                self.resistance += 1
                self.descRaça = ('Tritões guardam as profundezas do oceano, construindo pequenos assentamentos ao lado de trincheiras profundas, portais para os planos elementais e outros pontos perigosos longe dos olhos de pessoas ligadas à terra.\n•  Guardiões há muito estabelecidos no fundo do oceano profundo, nos últimos anos, os nobres tritões tornaram-se cada vez mais ativos no mundo acima.')
    def mostrarDescRaça(self):
        print(f'\n•  {(self.raça).upper()}  •\n{self.descRaça}')
    def skillclasse(self,classe):
        classe = self.classe
        match classe:
            case 'Bárbaro':
                self.descClasse = ('Um feroz guerreiro de origem primitiva que pode entrar em fúria durante uma batalha, é o guerreiro furioso e brutal que lutará até não poder mais.\n•  Sua fúria pode vir da raiva por um mundo injusto ou de seu instinto animal, concedendo-lhes força e resiliência sobre-humanas, essas fúrias geralmente são suficientes para derrotar seja lá o que está o ameaçando, após alguns usos desse reservatório de fúria o bárbaro descansa.\n•  Os bárbaros se sentem mais vivos em meio ao caos do combate.')

                self.prof = ('•  Armaduras leves, armaduras médias e escudos\n•  Armas simples, armas marciais\n•  Força, Constituição\n•  Adestrar Animais, Atletismo, Intimidação, Natureza, Percepção e Sobrevivência')

            case 'Bardo':
                self.descClasse = ('O bardo é um mestre da canção, discurso e a magia contida neles.\n•  As palavras dos deuses lhe derá forma ao multiverso, e os ecos dessas Palavras de Criação primordiais ainda ressoam através do cosmos.\n•  A música dos bardos é uma tentativa de capitar e aproveitar esses ecos, sutilmente tecidas em suas magias e poderes.')

                self.prof = ('•  Armaduras leves\n•  Armas simples, bestas de mão, espadas longas, rapieiras, espadas curtas\n•  Três instrumentos musicais, à sua escolha\n•  Destreza, Carisma')

            case 'Bruxo':
                self.descClasse = ('Os bruxos são desbravadores do conhecimento que existe escondido no tecido do multiverso.\n•  Através de pactos feitos com seres misteriosos detentores de poder sobrenatural, os bruxos desbloqueiam efeitos mágicos tão sutis quanto espetaculares.\n•  Extraindo o conhecimento antigo de seres como nobres fadas, demônios, diabos, bruxas e entidades alienígenas do Reino Distante, os bruxos remontam segredos arcanos para aprimorar seus próprios poderes.')

                self.prof = ('•  Armaduras leves\n•  Armas simples\n•  Sabedoria, Carisma\n•  Arcanismo, Enganação, História, Intimidação, Investigação, Natureza e Religião ')

            case 'Clérigo':
                self.descClasse = ('Clérigos são intermediadores entre o mundo mortal e o distante plano dos deuses.\n•  Tão variados quanto os deuses que servem, clérigos se esforçam para ser a própria mão de seus deuses.\n•  Não é apenas um sacerdote comum, mas alguém investido de poder divino.\n•  Eles podem causar medo e pavor, espalhar pragas ou venenos, e até lançar fogo divino para consumir seus inimigos.\n•  Combinam o poder mágico de curar e inspirar seus aliados com magias que ferem e debilitam seus inimigos.')

                self.prof = ('•  Armaduras Leves e Armaduras Médias e Escudos\n•  Todas as arma Simples\n•  Sabedoria e Carisma\n•  História, Intuição, Medicina, Persuasão e Religião')

            case 'Druida':
                self.descClasse = ('Os druidas reverenciam a natureza acima de tudo, adquirindo suas magias e outros poderes mágicos, ou da força da natureza per si ou de uma divindade da natureza.\n•  Muitos druidas buscam uma espiritualidade mística de união transcendental com a natureza ao invés de se devotarem a uma entidade divina, enquanto outros servem deuses da natureza selvagem, animais ou forças elementais.\n•  As antigas tradições druídicas, algumas vezes são chamadas de Crença Antiga, contrastando com a adoração de deuses em templos ou santuários.')

                self.prof = ('•  Armaduras leves, armaduras médias, escudos (não vestem armaduras ou usar escudos de metal)\n•  Clavas, adagas, dardos, azagaias, maças, bordões, cimitarras, foices, fundas e lanças.\n•  Kit de herbalismo\n•  Inteligência, Sabedoria\n•  Arcanismo, Adestrar Animais, Intuição, Medicina, Natureza, Percepção, Religião e Sobrevivência')

            case 'Feiticeiro':
                self.descClasse = ('Os feiticeiros carregam um patrimônio mágico conferido a eles por uma linhagem exótica, alguma influência de outro mundo ou exposição a forças cósmicas desconhecidas.\n•  Não é possível estudar feitiçaria como se aprende um idioma, assim como não se aprende a viver uma vida lendária.\n•  Ninguém escolhe a feitiçaria: os poderes escolhem o feiticeiro.\n•  Os feiticeiros são raros no mundo e é incomum encontrar um feiticeiro que não esteja envolvido na vida de aventuras de alguma forma.\n•  Pessoas com poder mágico fluindo em suas veias descobrem cedo que o poder não gosta de ficar quieto.\n•  A magia de um feiticeiro gosta de ser exercida e tem uma tendência de fluir de maneiras imprevisíveis se não for chamada.')

                self.prof = ('•  Adagas, dardos, fundas, bordões e bestas leves\n•  Constituição, Carisma\n•  Arcanismo, Enganação, Intuição, Intimidação, Persuasão e Religião')

            case 'Guardião':
                self.descClasse = ('Os guardiões são indivíduos vigorosos que recorrem aos espíritos primitivos da natureza para defender o mundo natural dos que o corrompem ou o destroem.\n•  Alguns guardiões utilizam o poder da terra e das rochas para proteger seus aliados do perigo, enquanto outros invocam a força primitiva de dentro de si para aumentar sua ferocidade e tenacidade.\n•  O poder primitivo está no solo, aos pés do guardião, pulsando com cada batida de seu coração e fluindo através de seus pulmões a cada respiração. O mundo clama por ele, chamando um campeão para defendê-lo.')

                self.prof = ('•  Todas as Armaduras, Escudos\n•  Corpo a corpo simples e Corpo a corpo militar\n•  Força e Constituição\n•  Acrobacia, Adestrar Animais, Atletismo, História, Intuição, Intimidação, Percepção e Sobrevivência')

            case 'Guerreiro':
                self.descClasse = ('Guerreiros tem maestria com armas e armaduras sem precedentes, bem como um vasto conhecimento e habilidades em combate.\n•  E eles estão bem familiarizados com a morte, seja simplesmente conhecendo-a ou desafiando-a cara a cara.\n•  Guerreiros aprendem o básico de todos os estilos de combate. Todo guerreiro sabe brandir um machado, esgrimir com uma rapieira, empunhar uma espada longa ou uma espada grande, usar um arco ou mesmo prender inimigos em uma rede com algum grau de perícia.\n•  Da mesma forma, um guerreiro sabe usar escudos e qualquer tipo de armadura. Além do conhecimento básico, cada guerreiro se especializa em certo estilo de combate.\n•  Tanto um Humano com armadura, um bando de Goblins, Elfos, Meios-Orcs, Anões, Gladeadores, Todos esses podem ser considerados Guerreiros.')

                self.prof = ('•  Todas as armaduras, escudos\n•  Armas simples, armas marciais\n•  Força, Constituição\n•  Acrobacia, Adestrar Animais, Atletismo, História, Intuição, Intimidação, Percepção e Sobrevivência')

            case 'Ladino':
                self.descClasse = ('Ladinos dedicam muito de seus recursos para se tornarem mestres em várias perícias, bem como aperfeiçoar suas habilidades em combate, adquirindo uma vasta experiência que poucos personagens podem alcançar.\n•  Muitos ladinos focam na furtividade e trapaça, enquanto outros refinam suas perícias para ajudá-los nas masmorras, como escalada, encontrar e desarmar armadilhas, e abrir fechaduras.\n•  Eles possuem uma habilidade especial para encontrar a solução para praticamente qualquer problema, demonstrando desenvoltura e versatilidade, a chave de qualquer grupo aventureiro de sucesso.')

                self.prof = ('•  Armaduras leves\n•  Armas simples, bestas de mão, espadas longas, rapieiras, espadas curtas\n•  Ferramentas de ladrão\n•  Destreza, Inteligência\n•  Acrobacia, Atletismo, Atuação, Enganação, Furtividade, Intimidação, Intuição, Investigação, Percepção, Persuasão e Prestidigitação')

            case 'Mago':
                self.descClasse = ('Selvagem e enigmático, Os magos são os detentores da magia arcana. Eles utilizam o verdadeiro poder que permeia o cosmos, pesquisam rituais esotéricos capazes de alterar o tempo e o espaço.\n•  Sua magia invoca monstros de outros planos de existência, vislumbra o futuro ou transforma inimigos mortos em zumbis.\n•  Suas magias mais poderosas podem transformar uma substância em outra, evocar meteoros que caem do céu ou abrir portais para outros mundos.\n•  O poder da magia atrai estudiosos que buscam dominar seus mistérios. Alguns aspiram ser como deuses, moldando a realidade à sua vontade.\n•  Magos vivem e morrem por suas magias. Todo o resto é secundário. Eles aprendem novas magias à medida que eles experimentam e crescem em experiência. Também podem aprender magias de outros magos, de tomos antigos ou escrituras, e de criaturas anciãs (como as fadas) que são imersas em magia.')

                self.prof = ('•  Adagas, dardos, fundas, bordões, bestas leves\n•  Inteligência, Sabedoria\n•  Arcanismo, História, Intuição, Investigação, Medicina e Religião')

            case 'Monge':
                self.descClasse = ('Monges fazem estudos cuidadosos da energia mágica que a maioria das tradições monásticas chama de chi.\n•  Essa energia é um elemento da mágica que inunda o multiverso, especificamente os elementos que fluem através dos corpos vivos.\n•   Os monges atrelam esse poder dentro de si mesmos para criar efeitos mágicos e exceder a capacidade física de seus corpos, e alguns dos seus ataques especiais podem bloquear o fluxo de chi nos seus oponentes.\n•  Usando essa energia, os monges canalizam velocidade e força incríveis em seus ataques desarmados.\n•  À medida que eles ganham experiência, seu treinamento marcial e sua maestria do chi lhe confere mais poder sobre seus corpos e sobre os corpos dos seus adversários.')

                self.prof = ('•  Armas simples, espadas curtas\n•  Ferramenta de artesão ou um instrumento musical\n•  Força, Destreza\n•  Acrobacia, Atletismo,Furtividade, História, Intuição e Religião')
    def mostrarDescClasse(self):
        print(f'\n•  {(self.classe).upper()}  •\n{self.descClasse}')
    def mostrarProf(self):
        print(f'Proeficiencias:\n{self.prof}')