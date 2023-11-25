from manim import *

class SnellsLaw(Scene):
    def construct(self):
        
        comprimento_linha = 6
        linha_horizontal = Line(start=LEFT*comprimento_linha, end=RIGHT*comprimento_linha, color=BLUE)

        self.play(Create(linha_horizontal))

        

        altura_da_linha_normal = 3
        linha_da_normal = DashedLine(
            start=DOWN*altura_da_linha_normal,
            end=UP * altura_da_linha_normal
        )
        texto_normal = Text("Normal", font_size=14).next_to(linha_da_normal, UP)


        self.play(Create(linha_da_normal), Write(texto_normal))

        
        comprimento_raio_luz = 3
        raio_luz_1= Line(
            start=ORIGIN ,
            end=UP * comprimento_raio_luz,
            color=RED,
        )

        raio_luz_2 = Line(
            start=ORIGIN,
            end= DOWN * comprimento_raio_luz,
            color=LIGHT_PINK
        )

        self.play(Create(raio_luz_1))
        self.play(Rotate(raio_luz_1, TAU / 8), about_point=ORIGIN, run_time=2)  # Girando 90 graus no sentido anti-horário
        self.play(Create(raio_luz_2))
        self.play(Rotate(raio_luz_2, TAU /12), about_point=ORIGIN, run_time=2)  # Girando 90 graus no sentido anti-horário

        chave_x = always_redraw(
            lambda:  BraceLabel( raio_luz_1, "x", brace_direction=DOWN)
        # Adicionando a chave à cena
        )

        chave_d = always_redraw(
            lambda: BraceLabel(Line(raio_luz_2.get_end(), raio_luz_1.get_end()), 'd', brace_direction=DOWN)
        )

        chave_ha = always_redraw(
            lambda: BraceLabel(raio_luz_1, r'h_a', brace_direction=LEFT)
        )
        chave_hw = always_redraw(
            lambda: BraceLabel(Line(ORIGIN+LEFT*2, raio_luz_2.get_end()+ LEFT*2), r'h_w', brace_direction=LEFT)
        )



        self.play(Create(chave_x))
        self.play(Create(chave_d))
        self.play(Create(chave_ha))
        self.play(Create(chave_hw))

        texto_raio1 = Text("Raio de luz", font_size=14).next_to(raio_luz_1, UP)
        texto_raio2 = Text("Raio de luz da refração", font_size=14).next_to(raio_luz_2, DOWN+ RIGHT)
        self.play(Write(texto_raio1), Write(texto_raio2))
        self.wait(1)
        
        #rotacionando pra esquerda
        self.play(
            Rotate(raio_luz_1, TAU / 16),
            Rotate(raio_luz_2, TAU/18)
             ,about_point=ORIGIN, run_time=2
            )  

        self.wait(1)

        #voltando da rotacao feita
        self.play(
            Rotate(raio_luz_1, -TAU / 16),
            Rotate(raio_luz_2, -TAU/18)
             ,about_point=ORIGIN, run_time=2
        )  

        self.wait(1)
        self.play(FadeOut(texto_raio1, texto_raio2))
        texto1 = Text('Aumentando o índice de refração', font_size=16 )
        texto1.to_edge(UP+RIGHT)
        self.play(Write(texto1))
        self.wait(1)

        self.play(Rotate(raio_luz_2, -TAU/22)
             ,about_point=ORIGIN, run_time=2)

        self.wait(1)

        self.remove(texto1)
        self.play(Rotate(raio_luz_2, TAU/22)
             ,about_point=ORIGIN, run_time=2)

        
        self.wait(1)