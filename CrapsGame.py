using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.UI;
using UnityEditor;
using Unity.VisualScripting;


public class crapsGame : MonoBehaviour
{
    public TextMeshProUGUI joueur;
    public TextMeshProUGUI montant;
    public GameObject premierePage;
    public GameObject deuxiemePage;
    public GameObject lesDes;
    public TMP_InputField nom;
    public TMP_InputField montantInitial;
    public Button enregistrer;
    public Button btn200;
    public Button btn25;
    public Button btn5;
    public Button btn1;
    public Button btnAnnuler;
    public Button btnlancer;
    public TextMeshProUGUI jeton;
    public TextMeshProUGUI nomDuJoueur;
    public TextMeshProUGUI mise;
    public TextMeshProUGUI montantArgent;
    public TextMeshProUGUI miseArgent;
    public TextMeshProUGUI de1;
    public TextMeshProUGUI de2;
    public TextMeshProUGUI resultatText;
    private int miser = 0;
    private int montantActuel;
    private int nb1;
    private int nb2;
    private int somme;
    private int temp = 0;
    private bool jeuEnProgres;

    public void enregistrerNom()
    {
        jeuEnProgres = false;
        if (nom.text == "")
        { 
            Debug.Log("Entrez votre nom."); 
        }
        
        if (int.TryParse(montantInitial.text, out montantActuel))
        {
            if (montantActuel <= 0)
            {
                Debug.Log("Entrez un nombre entier plus grand que 0.");
            }
        }
        else
        {
            Debug.Log("Entrez un nombre valide pour le montant.");
        }
        
        premierePage.gameObject.SetActive(false);
        deuxiemePage.gameObject.SetActive(true);
        nomDuJoueur.text = nom.text;
        mise.text = "Mise: ";
        montantArgent.text = montantActuel.ToString() + ".00$";
        miseArgent.text = miser.ToString() + ".00$";
        if (miser > 0)
        {
            btnlancer.gameObject.SetActive(true);
        }
        else
        {
            btnlancer.gameObject.SetActive(false);
        }
    }
    public void ajouter5()
    {
        if (montantActuel >= 5 && jeuEnProgres==false)
        {
            montantActuel -= 5;
            montantArgent.text = montantActuel.ToString() + ".00$";

            miser += 5;
            miseArgent.text = miser.ToString() + ".00$";
            resultatText.text = "";
        }
        if (miser > 0)
        {
            btnlancer.gameObject.SetActive(true);
        }
        else
        {
            btnlancer.gameObject.SetActive(false);
        }

    }
    public void ajouter200()

    {
        if (montantActuel >= 200 && jeuEnProgres == false)
        {
            montantActuel -= 200;
            montantArgent.text = montantActuel.ToString() + ".00$";

            miser += 200;
            miseArgent.text = miser.ToString() + ".00$";
            resultatText.text = "";
        }
        if (miser > 0)
        {
            btnlancer.gameObject.SetActive(true);
        }
        else
        {
            btnlancer.gameObject.SetActive(false);
        }
    }
    public void ajouter25()

    {
        if (montantActuel >= 25 && jeuEnProgres == false)
        {
            montantActuel -= 25;
            montantArgent.text = montantActuel.ToString() + ".00$";

            miser += 25;
            miseArgent.text = miser.ToString() + ".00$";
            resultatText.text = "";
        }
        if (miser > 0)
        {
            btnlancer.gameObject.SetActive(true);
        }
        else
        {
            btnlancer.gameObject.SetActive(false);
        }
    }
    public void ajouter1()

    {
        if (montantActuel >= 1 && jeuEnProgres == false)
        {
            montantActuel -= 1;
            montantArgent.text = montantActuel.ToString() + ".00$";

            miser += 1;
            miseArgent.text = miser.ToString() + ".00$";
            resultatText.text = "";
        }
        if (miser > 0)
        {
            btnlancer.gameObject.SetActive(true);
        }
        else
        {
            btnlancer.gameObject.SetActive(false);
        }
    }
    public void annuler()
    {
        if (jeuEnProgres == false)
        {
            montantActuel += miser;
            montantArgent.text = montantActuel.ToString() + ".00$";
            miser = 0;
            miseArgent.text = miser.ToString() + ".00$";
            if (miser > 0)
            {
                btnlancer.gameObject.SetActive(true);
            }
            else
            {
                btnlancer.gameObject.SetActive(false);
            }
        }
    }
    public void lancer()
    {
        jeuEnProgres = true;
        resultatText.text = "";
        lesDes.gameObject.SetActive(true);
        nb1 = Random.Range(1, 7);
        de1.text = nb1.ToString();
        nb2 = Random.Range(1, 7);
        de2.text = nb2.ToString();
        somme = nb1 + nb2;
        jeton.text = somme.ToString();
        if (temp == 0)
        {
            if (somme == 7 || somme == 11)
            {
                resultatText.gameObject.SetActive(true);
                resultatText.text = "Vous avez gagn� " + miser.ToString() + ".00 $";
                jeton.text = "OFF";
                montantActuel += miser * 2;
                temp = 0;
                miser = 0;
                miseArgent.text = miser.ToString()+".00$";
                montantArgent.text = montantActuel.ToString() + ".00 $";
                btnlancer.gameObject.SetActive(false);
                jeuEnProgres = false;
            }
            else if (somme == 2 || somme == 3 || somme == 12)
            {
                resultatText.gameObject.SetActive(true);
                resultatText.text = "Vous avez perdu " + miser.ToString() + ".00 $";
                jeton.text = "OFF";
                temp = 0;
                miser = 0;
                miseArgent.text = miser.ToString() + ".00$";
                btnlancer.gameObject.SetActive(false);
                jeuEnProgres = false;
            }
            else
            {
                temp = somme;

                resultatText.gameObject.SetActive(false);
                jeuEnProgres = true;
            }
        }
        else
        {
            if (somme == temp)
            {
                resultatText.gameObject.SetActive(true);
                resultatText.text = "Vous avez gagn� " + miser.ToString() + ".00 $";
                jeton.text = "OFF";
                montantActuel += miser * 2;
                miser = 0;
                temp = 0;
                miseArgent.text = miser.ToString() + ".00$";
                montantArgent.text = montantActuel.ToString() + ".00 $";
                btnlancer.gameObject.SetActive(false);
                jeuEnProgres = false;
            }
            else if (somme == 7)
            {
                resultatText.gameObject.SetActive(true);
                resultatText.text = "Vous avez perdu " + miser.ToString() + ".00 $";
                jeton.text = "OFF";
                miser = 0;
                temp = 0;
                miseArgent.text = miser.ToString() + ".00$";
                btnlancer.gameObject.SetActive(false);
                jeuEnProgres = false;
            }
        }
        
    }

        
        
    
     
    // Start is called before the first frame update
    void Start()
    {
        jeuEnProgres=false;
        joueur.text = "Joueur: ";
        montant.text = "Montant: ";
        jeton.text = "OFF";
        deuxiemePage.gameObject.SetActive(false);
        lesDes.gameObject.SetActive(false);
        btnlancer.gameObject.SetActive(false);
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}

