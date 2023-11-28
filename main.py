from manim import *

class SnellsLaw(MovingCameraScene):
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
            color=LIGHT_GREY
        )

        self.play(
            Create(raio_luz_1),
            Create(raio_luz_2)
            )
        self.play(Rotate(raio_luz_1, TAU / 8), about_point=ORIGIN, run_time=1)  # Girando 90 graus no sentido anti-horário
        self.play(Rotate(raio_luz_2, TAU /12), about_point=ORIGIN, run_time=1)  # Girando 90 graus no sentido anti-horário
        
        #adicionando angulos
        angulo_theta_1 = always_redraw(
            lambda: Angle(raio_luz_1, linha_horizontal, radius=0.5, quadrant=(1,-1))
        )
        texto_theta_1= always_redraw(
            lambda:MathTex(r'\theta_1', font_size=24, color=RED).next_to(angulo_theta_1, ORIGIN+LEFT/2)
        )
        
        angulo_theta_2 = always_redraw(
            lambda: Angle(linha_da_normal, raio_luz_2, radius=0.5, quadrant=(-1,1))
        )
        texto_theta_2 = always_redraw(
            lambda:MathTex(r'\theta_2', font_size=24, color=RED).next_to(angulo_theta_2, ORIGIN+DOWN/2)
        )
        

    

        self.play(Create(angulo_theta_1), Create(angulo_theta_2))
        self.play(Create(texto_theta_1), Create(texto_theta_2))
        

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

        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=linha_horizontal.width*1.8).move_to(RIGHT*6))
        
        texto_fermat = Text('Príncipio de Fermat: A luz sempre percorrerá o caminho que gaste o menor tempo', font_size=22)
        texto_fermat.move_to(RIGHT*5+UP*4)
        self.play(Write(texto_fermat),run_time=1)

     
        #grafico do tempo
        axes  = Axes(x_range=(-1,5), y_range=(-1,10))
        labels = axes.get_axis_labels(
            Tex("x"), Tex("t")
        )
        labels.move_to(RIGHT*10)
        axes.set_color([BLUE, GREEN])

        axes.move_to(RIGHT*10)

        self.play(Create(axes))
        self.add(labels)
        
        parabola = axes.plot(lambda x: x**2 -5*x+7)
        parabola.set_stroke(BLUE)
        self.play(
            Create(parabola)
        )
        self.wait()

        # You can use axes.input_to_graph_point, abbreviated
        # to axes.i2gp, to find a particular point on a graph
        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(0, parabola))
        self.play(FadeIn(dot, scale=0.8))

        # A value tracker lets us animate a parameter, usually
        # with the intent of having other mobjects update based
        # on the parameter
        x_tracker = ValueTracker(0)
        f_always(
            dot.move_to,
            lambda: axes.i2gp(x_tracker.get_value(), parabola)
        )

        

        rotacionar_raios_maior_angulo = AnimationGroup(
            Rotate(raio_luz_1, TAU / 16, about_point=ORIGIN),
            Rotate(raio_luz_2, TAU/18,  about_point=ORIGIN),
            run_time=2
            )
        
        self.play(
            rotacionar_raios_maior_angulo,
            x_tracker.animate.set_value(4),
            run_time=3
           )
        
        rotacionar_raio_para_menor_angulo = AnimationGroup(
            Rotate(raio_luz_1, -TAU / 20, about_point=ORIGIN),
            Rotate(raio_luz_2, -TAU/24,  about_point=ORIGIN),
            run_time=2
        )
        #voltando da rotacao feita
        self.play(
            rotacionar_raio_para_menor_angulo,
            x_tracker.animate.set_value(2.5),
            run_time=2
            )  

        
        #self.play(self.camera.frame.animate.set(width=linha_horizontal.width*1.8).move_to(RIGHT*6))

    
        self.wait(1)