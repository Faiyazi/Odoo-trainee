import { registry } from "@web/core/registry";
import { Component, xml } from "@odoo/owl";

class SepiaEffect extends Component {
  static template = xml`
    <div>
        <style>
            @keyframes sepiaInOut {
                    0%   { opacity: 0; }
                    25%  { opacity: 1; }
                    75%  { opacity: 1; }
                    100% { opacity: 0; }
                  }
        </style>

        <div id="sepiaOverlay" style="
                  position: fixed;
                  inset: 0;
                  display: flex;
                  justify-content: center;
                  align-items: center;
                  pointer-events: none;
                  animation: sepiaInOut 4s ease-in-out forwards;
                  z-index: 99999;
                ">
        <div style="display:flex; flex-direction:column; align-items:center;">
                    <img src="/owl_js/static/src/img/shopping-cart.gif" style="
                      width: 100%;
                      max-width: 250px;
                      opacity: 0.3;
                      animation: sepiaInOut 4s ease-in-out forwards;
                    "/>
                    <div style="color: black; font-size: 20px; margin-top: 10px;"> <t t-esc="props.message"/> </div>
                  </div>
                </div>
    </div>

              <style>
              @keyframes sepiaInOut {
                  0%   { opacity: 0; }
                  25%  { opacity: 1; }   
                  75%  { opacity: 1; }   
                  100% { opacity: 0; }  
              }
              </style>

              <script>
              setTimeout(() => {
                  document.getElementById('sepiaOverlay')?.remove();
              }, 2000);
              </script>

  `;
}

export function sepiaEffectProvider(env, params = {}) {
  let message = params.message;

  if (message instanceof Element) {
    message = message.outerHTML;
  } else if (!message) {
    message = "Thank You!";
  }

  const props = {
    imgUrl: params.img_url || "/owl_js/static/src/img/shopping-cart.gif",
    fadeout: params.fadeout || "medium",
    message,
  };

  return {
    Component: SepiaEffect,
    props,
  }

  env.services.notification.add(message);
}
const effectRegistry = registry.category("effects");
effectRegistry.add("cart", sepiaEffectProvider);