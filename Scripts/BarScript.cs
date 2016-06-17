using UnityEngine;
using System.Collections;
using UnityEngine.UI;

public class BarScript : MonoBehaviour {
	
	public WepScript wpScript;
	public WepShotgun wpShotgun;
	public WepMelee wpMelee;
	public WepMarker wpMarker;

	[SerializeField]
	private float fillAmount = 1;

	[SerializeField]
	private Image content;



	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
		HandleBar ();
	}

	private void HandleBar(){
		if (wpScript.currentWeapon == 2){
			content.fillAmount = (wpShotgun.currRounds / (float)wpShotgun.magazineSize);
		} else if (wpScript.currentWeapon == 3){
			content.fillAmount = (wpMarker.currRounds / (float)wpMarker.totalAmmo);
		}
	}
}
