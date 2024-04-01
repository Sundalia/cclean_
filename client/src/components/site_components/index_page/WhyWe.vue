<template>
  <div class="main_h2__header_box">
    <h2 class="main_h2">ПОЧЕМУ СТОИТ ВЫБРАТЬ НАС</h2>
  </div>

  <div class="why_we__block_grid_container">
    <div class="col why_we__block_grid">

      <div class="row why_we__block">
        <div class="row why_we__block_header_wraper">
            <img class="why_we__block_img" src="../../../assets/why_we/pig.svg"/>
            <h3 class="why_we__block_header">ПРОЗРАЧНОЕ ЦЕНООБРАЗОВАНИЕ</h3>
        </div>
        <div class="why_we__block_text_wrapper">
          <p class="why_we__block_text">
            Работая с нами вы получаете гарантию оплаты исключительно за проделанную работу, 
            <span class="why_we__block_text-orange">
              &nbsp;без скрытых доплат
            </span>
            , авансов и навязанных услуг
          </p>
        </div>
      </div>

      <div class="row why_we__block">
        <div class="row why_we__block_header_wraper">
            <img class="why_we__block_img" src="../../../assets/why_we/robot.svg"/>
            <h3 class="why_we__block_header">ПРОФЕССИОНАЛЬНАЯ ТЕХНИКА</h3>
        </div>
        <div class="why_we__block_text_wrapper">
          <p class="why_we__block_text">
            В нашем арсенале есть  
            <span class="why_we__block_text-orange">
              &nbsp;всё
            </span>
            профессиональное оборудование для выполнения клининговых услуг высокого качества.
          </p>
        </div>
      </div>

      <div class="row why_we__block">
        <div class="row why_we__block_header_wraper">
            <img class="why_we__block_img" src="../../../assets/why_we/colba.svg"/>
            <h3 class="why_we__block_header">ВЫЕЗД НА КЛИН-ТЕСТ БЕСПЛАТНО</h3>
        </div>
        <div class="why_we__block_text_wrapper">
          <p class="why_we__block_text">
            Наш менеджер  
            <span class="why_we__block_text-orange">
              &nbsp;бесплатно
            </span>
            приедет к вам для оценки объёма работ и стоимости услуг.
          </p>
        </div>
      </div>

      <div class="row why_we__block">
        <div class="row why_we__block_header_wraper">
            <img class="why_we__block_img" src="../../../assets/why_we/keys.svg"/>
            <h3 class="why_we__block_header">ДОСТАВКА КЛЮЧЕЙ</h3>
        </div>
        <div class="why_we__block_text_wrapper">
          <p class="why_we__block_text">
            Если вы не можете находиться на объекте во время уборки, или вам нужно будет по окончании работ быть в другом месте,   
            <span class="why_we__block_text-orange">
              &nbsp;мы можем привезти
            </span>
            вам ключи
          </p>
        </div>
      </div>

      <div class="row why_we__block">
        <div class="row why_we__block_header_wraper">
            <img class="why_we__block_img" src="../../../assets/why_we/dogovor.svg"/>
            <h3 class="why_we__block_header">ДОГОВОР И АКТ ПРИЁМКИ</h3>
        </div>
        <div class="why_we__block_text_wrapper">
          <p class="why_we__block_text">
            Чтобы   
            <span class="why_we__block_text-orange">
              &nbsp;избежать недопониманий
            </span>
            , требуемый фронт работ описывается в прейскуранте и акте приема работ, так же подписывается договор на оказание услуг.
          </p>
        </div>
      </div>

      <div class="row why_we__block">
        <div class="row why_we__block_header_wraper">
            <img class="why_we__block_img" src="../../../assets/why_we/medal.svg"/>
            <h3 class="why_we__block_header">ГАРАНТИЯ КАЧЕСТВА: 2 ДНЯ!</h3>
        </div>
        <div class="why_we__block_text_wrapper">
          <p class="why_we__block_text">
            Даём гарантию качества  
            <span class="why_we__block_text-orange">
              &nbsp;2 дня
            </span>
            на выполненные нами работы с момента их завершения.
          </p>
        </div>
      </div>

    </div>

  </div>
</template>

<script>


export default({
    name: 'WhyWe',

})
</script>

<style lang="scss" scoped>
.why_we__block_grid_container {
  display: flex;
  width: 100%;
  justify-content: center;
  align-items: center;
}

.why_we__block_grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  margin: 30px;
  grid-gap: 1.1px;
  background: $accent;
}

.why_we__block {
  padding: 5%;
  display: flex;
  justify-content: center;
  min-width: 250px;
  background: $background;
}

.why_we__block_img {
  margin-bottom: 10px;
  margin-right: 10px;
  width: 30px;
}

.why_we__block_header {
  font-family: 'Oswald';
  font-size: 1rem;
  line-height: 1.1rem;
  font-weight: bold;
  letter-spacing: 0;
  max-width: 150px;
}

.why_we__block_text_wrapper {
  display: flex;
  margin: 5%;
  justify-content: center;
}

.why_we__block_text {
  margin: 0;
  font-family: 'Comfortaa';
  text-align: center;
  font-size: 1rem;
  width: 90%;

}

.why_we__block_text-orange{
  color: $accent;
}

@media screen and (max-width: 820px) {
  .why_we__block_grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media screen and (max-width: 520px) {
  .why_we__block_grid {
    grid-template-columns: repeat(1, 1fr);
  }
}

</style>